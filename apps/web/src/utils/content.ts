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

export function loadDocs(lang?: string): Doc[] {
  const langs = lang ? [lang] : safeReadDir(contentRoot);
  const docs: Doc[] = [];
  for (const itemLang of langs) {
    const dir = path.join(contentRoot, itemLang, 'daily');
    for (const file of safeReadDir(dir)) {
      if (!file.endsWith('.md')) continue;
      const raw = fs.readFileSync(path.join(dir, file), 'utf-8');
      const { meta, body } = parseFrontmatter(raw);
      const slug = meta.slug || file.replace(/\.md$/, '');
      docs.push({
        meta,
        body,
        lang: itemLang,
        slug,
        url: `/${itemLang}/daily/${slug}/`,
      });
    }
  }
  return docs.sort((a, b) => String(b.meta.date).localeCompare(String(a.meta.date)) || b.slug.localeCompare(a.slug));
}

export function loadBriefs(lang: string) {
  return loadDocs(lang).filter((doc) => doc.meta.page_type === 'brief');
}

export function loadDoc(lang: string, slug: string) {
  return loadDocs(lang).find((doc) => doc.slug === slug);
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

  for (const line of lines) {
    if (!line.trim()) {
      closeList();
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
      out.push(`<h${level}>${inline(heading[2])}</h${level}>`);
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

function inline(text: string) {
  return escapeHtml(text)
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>');
}

function escapeHtml(text: string) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}
