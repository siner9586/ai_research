import fs from 'node:fs';
import path from 'node:path';

const repoRoot = path.resolve(process.cwd(), '../..');
const contentRoot = path.join(repoRoot, 'data/content');
const configsRoot = path.join(repoRoot, 'configs');

export type Doc = {
  meta: Record<string, any>;
  body: string;
  lang: string;
  slug: string;
  url: string;
  filePath: string;
  mtimeMs: number;
};

export function loadSite() {
  return {
    zh: {
      name: 'AI 研究简报',
      tagline: '从 arXiv 与公开信号中筛出值得跟进的 AI 论文',
    },
    en: {
      name: 'AI Research Brief',
      tagline: 'Source-first daily briefs for AI papers worth tracking',
    },
  };
}

export function loadTopics() {
  const file = path.join(configsRoot, 'topics.yaml');
  const text = fs.existsSync(file) ? fs.readFileSync(file, 'utf-8') : '';
  const rows: any[] = [];
  let current: any = null;
  for (const line of text.split('\n')) {
    if (line.startsWith('  - slug:')) {
      if (current) rows.push(current);
      current = { slug: line.split(':').slice(1).join(':').trim() };
    } else if (current && line.match(/^    (zh|en):/)) {
      const [key, ...rest] = line.trim().split(':');
      current[key] = rest.join(':').trim();
    }
  }
  if (current) rows.push(current);
  return rows;
}

export function loadDocs(lang?: string, options: { includeInternal?: boolean } = { includeInternal: true }): Doc[] {
  const langs = lang ? [lang] : safeReadDir(contentRoot);
  const docs: Doc[] = [];
  for (const itemLang of langs) {
    const dir = path.join(contentRoot, itemLang, 'daily');
    for (const file of safeReadDir(dir)) {
      if (!file.endsWith('.md')) continue;
      const filePath = path.join(dir, file);
      const raw = fs.readFileSync(filePath, 'utf-8');
      const { meta, body } = parseFrontmatter(raw);
      const slug = meta.slug || file.replace(/\.md$/, '');
      const isInternal = meta.page_type === 'sources' || slug.endsWith('-sources');
      if (isInternal && options.includeInternal === false) continue;
      const stat = fs.statSync(filePath);
      docs.push({
        meta,
        body,
        lang: itemLang,
        slug,
        url: `/${itemLang}/daily/${slug}/`,
        filePath,
        mtimeMs: stat.mtimeMs,
      });
    }
  }
  return docs.sort(compareDocs);
}

export function loadBriefs(lang: string) {
  return dedupeBriefsByDate(
    loadDocs(lang, { includeInternal: false })
      .filter((doc) => doc.meta.page_type === 'brief')
      .filter((doc) => String(doc.meta.date || '') <= beijingToday())
  );
}

export function loadSourceDocs(lang: string) {
  return loadDocs(lang, { includeInternal: true }).filter((doc) => doc.meta.page_type === 'sources');
}

export function loadDoc(lang: string, slug: string) {
  return loadDocs(lang, { includeInternal: true }).find((doc) => doc.slug === slug);
}

export function topicCounts(lang: string) {
  const counts: Record<string, number> = {};
  for (const doc of loadBriefs(lang)) {
    for (const tag of doc.meta.tags || []) {
      counts[tag] = (counts[tag] || 0) + 1;
    }
  }
  return counts;
}

export function displayBriefTitle(title: string | undefined | null) {
  return String(title || '')
    .replace(/^今日重点[:：]\s*/, '')
    .replace(/^Today's focus:\s*/i, '')
    .trim();
}

export function beijingToday() {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Shanghai',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(new Date());
}

export function markdownToHtml(markdown: string) {
  const lines = markdown.split('\n');
  const out: string[] = [];
  let inList = false;
  const closeList = () => {
    if (inList) {
      out.push('</ul>');
      inList = false;
    }
  };

  for (const rawLine of lines) {
    const line = normalizeDisplayLine(rawLine);
    if (!line.trim()) {
      closeList();
      continue;
    }
    if (line.startsWith('<p class="paper-meta-line">')) {
      closeList();
      out.push(line);
      continue;
    }
    if (line.startsWith('|')) {
      closeList();
      out.push(`<pre class="table-line">${escapeHtml(line)}</pre>`);
      continue;
    }
    const heading = line.match(/^(#{1,3})\s+(.*)$/);
    if (heading) {
      closeList();
      const level = heading[1].length;
      const h1Attrs = level === 1
        ? ' class="daily-brief-title" style="font-size: clamp(28px, 4.2vw, 34px); line-height: 1.18; letter-spacing: -0.025em;"'
        : '';
      out.push(`<h${level}${h1Attrs}>${inline(heading[2])}</h${level}>`);
      continue;
    }
    const item = line.match(/^-\s+(.*)$/);
    if (item) {
      if (!inList) {
        out.push('<ul>');
        inList = true;
      }
      out.push(`<li>${inline(item[1])}</li>`);
      continue;
    }
    const nestedItem = line.match(/^\s+-\s+(.*)$/);
    if (nestedItem) {
      if (!inList) {
        out.push('<ul>');
        inList = true;
      }
      out.push(`<li>${inline(nestedItem[1])}</li>`);
      continue;
    }
    closeList();
    out.push(`<p>${inline(line)}</p>`);
  }
  closeList();
  return out.join('\n');
}

function parseFrontmatter(raw: string) {
  const match = raw.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: raw };
  const meta: Record<string, any> = {};
  for (const line of match[1].split('\n')) {
    const index = line.indexOf(':');
    if (index === -1) continue;
    const key = line.slice(0, index).trim();
    const value = line.slice(index + 1).trim();
    try {
      meta[key] = JSON.parse(value);
    } catch {
      meta[key] = /^\d+$/.test(value) ? Number(value) : value.replace(/^"|"$/g, '');
    }
  }
  return { meta, body: match[2] };
}

function safeReadDir(dir: string) {
  return fs.existsSync(dir) ? fs.readdirSync(dir) : [];
}

function normalizeDisplayLine(line: string) {
  return line
    .replace(/^(#{1,6}\s*)今日重点[:：]\s*/, '$1')
    .replace(/^(#{1,6}\s*)Today's focus:\s*/i, '$1')
    .replace(/^今日重点[:：]\s*/, '')
    .replace(/^Today's focus:\s*/i, '');
}

function inline(text: string) {
  return escapeHtml(text)
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\[(.*?)\]\((.*?)\)/g, (_match, label, href) => {
      const className = isPaperLink(label, href) ? ' class="paper-meta-link"' : '';
      return `<a${className} href="${href}">${label}</a>`;
    });
}

function escapeHtml(text: string) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

export function dedupeBriefsByDate(docs: Doc[]) {
  const byDate = new Map<string, Doc>();
  for (const doc of docs.sort(compareDocs)) {
    const date = String(doc.meta.date || '');
    if (!date) continue;
    const existing = byDate.get(date);
    if (!existing || compareDocs(doc, existing) < 0) {
      byDate.set(date, doc);
    }
  }
  return Array.from(byDate.values()).sort(compareDocs);
}

function compareDocs(a: Doc, b: Doc) {
  const dateCompare = String(b.meta.date || '').localeCompare(String(a.meta.date || ''));
  if (dateCompare) return dateCompare;
  const generatedCompare = String(b.meta.generated_at || '').localeCompare(String(a.meta.generated_at || ''));
  if (generatedCompare) return generatedCompare;
  const countCompare = Number(b.meta.candidate_count || 0) - Number(a.meta.candidate_count || 0);
  if (countCompare) return countCompare;
  const mtimeCompare = b.mtimeMs - a.mtimeMs;
  if (mtimeCompare) return mtimeCompare;
  return b.slug.localeCompare(a.slug);
}

function isPaperLink(label: string, href: string) {
  return label === 'PDF' || /arxiv\.org\/(abs|pdf)\//.test(href) || /^\d{4}\.\d{4,5}$/.test(label);
}
