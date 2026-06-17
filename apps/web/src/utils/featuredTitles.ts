export type FeaturedTitleDoc = {
  meta?: Record<string, any>;
  body?: string;
};

export type FeaturedPaperTitle = {
  title: string;
  url: string;
};

export function getFeaturedPaperTitleItems(doc: FeaturedTitleDoc | undefined | null, lang: 'zh' | 'en' = 'zh', limit = 6): FeaturedPaperTitle[] {
  if (!doc) return [];
  const meta = doc.meta || {};
  const structuredTitles = lang === 'zh'
    ? firstStringArray(meta.featured_paper_titles_zh, meta.featured_titles_zh, meta.featured_paper_titles, meta.featured_titles)
    : firstStringArray(meta.featured_paper_titles_en, meta.featured_paper_titles, meta.featured_titles);
  const structuredUrls = firstStringArray(meta.featured_paper_urls, meta.featured_urls, meta.paper_urls);
  const parsed = structuredTitles.length > 0
    ? structuredTitles.map((title, index) => ({ title, url: structuredUrls[index] || '' }))
    : extractTitleItemsFromBody(doc.body || '', Number(meta.featured_count || limit) || limit);

  const seen = new Set<string>();
  const items: FeaturedPaperTitle[] = [];
  for (const item of parsed) {
    const cleanTitle = normalizeTitle(item.title || '');
    if (!cleanTitle) continue;
    const localizedTitle = lang === 'zh' ? localizePaperTitleZh(cleanTitle) : cleanTitle;
    const key = localizedTitle.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    items.push({ title: localizedTitle, url: String(item.url || '').trim() });
    if (items.length >= limit) break;
  }
  return items;
}

export function getFeaturedPaperTitles(doc: FeaturedTitleDoc | undefined | null, lang: 'zh' | 'en' = 'zh', limit = 6): string[] {
  return getFeaturedPaperTitleItems(doc, lang, limit).map((item) => item.title);
}

export function renderFeaturedPaperTitlesHtml(items: FeaturedPaperTitle[] | string[], lang: 'zh' | 'en' = 'zh'): string {
  const normalized = normalizeItems(items);
  if (!normalized.length) return '';
  const heading = lang === 'zh' ? '本期重点' : 'Featured';
  const itemsHtml = normalized
    .map((item, index) => {
      const link = item.url
        ? `<a class="featured-paper-link" href="${escapeHtml(item.url)}" aria-label="${lang === 'zh' ? '打开原论文：' : 'Open source paper: '}${escapeHtml(item.title)}" target="_blank" rel="noopener noreferrer">🔗</a>`
        : '';
      return `<li><span class="featured-paper-index">${index + 1}</span><span class="featured-paper-title-text">${escapeHtml(item.title)}${link}</span></li>`;
    })
    .join('');
  return `<section class="featured-paper-digest" aria-label="${heading}"><p class="featured-paper-digest-kicker">${heading}</p><ol class="featured-paper-digest-list">${itemsHtml}</ol></section>`;
}

function normalizeItems(items: FeaturedPaperTitle[] | string[]): FeaturedPaperTitle[] {
  return items.map((item) => typeof item === 'string' ? { title: item, url: '' } : item).filter((item) => item.title);
}

function firstStringArray(...values: any[]): string[] {
  for (const value of values) {
    if (Array.isArray(value)) {
      const rows = value.map((item) => String(item || '').trim()).filter(Boolean);
      if (rows.length) return rows;
    }
  }
  return [];
}

function extractTitleItemsFromBody(body: string, limit: number): FeaturedPaperTitle[] {
  const titles: FeaturedPaperTitle[] = [];
  const regex = /<p class="paper-meta-line"><span>(.*?)<\/span>\s*<a class="paper-meta-link" href="([^"]+)"/g;
  let match: RegExpExecArray | null;
  while ((match = regex.exec(body)) && titles.length < limit) {
    const title = normalizeTitle(stripTrailingAuthors(decodeHtml(match[1])));
    const url = decodeHtml(match[2]);
    if (title) titles.push({ title, url });
  }
  return titles;
}

function stripTrailingAuthors(value: string): string {
  return value.replace(/\s+\([^()]*\)\s*$/, '').trim();
}

function normalizeTitle(value: string): string {
  return value.replace(/\s+/g, ' ').replace(/\s+([:：,，;；])/g, '$1').trim();
}

function decodeHtml(value: string): string {
  return value
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function escapeHtml(value: string): string {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function localizePaperTitleZh(title: string): string {
  const exact: Record<string, string> = {
    'A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction': '一种利用远程数据科学进行跨机构学生留存预测的隐私保护框架',
    'Rigel: Reverse-Engineering the Metal 4.1 Tensor Compute Path on the Apple M4 Max GPU': 'Rigel：逆向解析 Apple M4 Max GPU 上 Metal 4.1 张量计算路径',
    'EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery': 'EurekAgent：面向自主科学发现的 Agent 环境工程',
    'AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility': 'AgentBeats：面向开放性、标准化与可复现性的 Agent 化评测框架',
    'SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale': 'SPARC：从大规模机器人示范中生成可靠空间标注',
    'Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities': 'Mod-Guide：面向原住民、少数族裔与宗教少数群体不敏感言论的 LLM 内容审核反馈系统',
    'An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics': '面向湿实验室机器人的具身仿真平台、基准与数据高效增强框架',
    'MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems': 'MAStrike：面向多智能体系统的 Shapley 引导合谋红队测试',
    'SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings': 'SafeLLM：安全关键场景中以抽取替代改写的抗幻觉方案',
    'LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning': 'LongSpike：用于高效长序列学习的分数阶脉冲状态空间模型',
    'SMGFM: Spectral Multimodal Graph Pretraining for Multimodal-Attributed Graphs': 'SMGFM：面向多模态属性图的谱域多模态图预训练',
    'LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories': 'LabVLA：将视觉-语言-动作模型落地到科学实验室',
    'ActiveSAM: Image-Conditional Class Pruning for Fast and Accurate Open-Vocabulary Segmentation': 'ActiveSAM：面向快速准确开放词汇分割的图像条件类别剪枝',
    'ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control': 'ARB4WM：面向连续控制世界模型的对抗鲁棒性基准',
    'When Confidence Lacks Concepts: Interpretable OOD Detection via Representation Perturbations': '当置信度缺少概念：基于表征扰动的可解释分布外检测',
    'Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models': '无信号选择与表达恢复：面向冻结小型代码模型的事后证伪算子测量研究',
    'Semantic Flip: Synthetic OOD Generation for Robust Refusal in Embodied Question Answering and Spatial Localization': '语义翻转：面向具身问答与空间定位鲁棒拒答的合成式分布外样本生成',
    'Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment': '解耦语义与失真：面向 AI 生成图像质量评估的多尺度双流视觉语言对齐',
  };
  if (exact[title]) return exact[title];

  let text = title;
  const phraseRules: Array<[RegExp, string]> = [
    [/^A\s+/i, '一种'],
    [/^An\s+/i, '一种'],
    [/^The\s+/i, ''],
    [/Privacy-Preserving/gi, '隐私保护'],
    [/Remote Data Science/gi, '远程数据科学'],
    [/Inter-Institutional/gi, '跨机构'],
    [/Student Retention Prediction/gi, '学生留存预测'],
    [/Embodied Simulation Platform/gi, '具身仿真平台'],
    [/Wet-Lab Robotics/gi, '湿实验室机器人'],
    [/Data-Efficient Augmentation Framework/gi, '数据高效增强框架'],
    [/Shapley-Guided/gi, 'Shapley 引导'],
    [/Collusive Red-Teaming/gi, '合谋红队测试'],
    [/Multi-Agent Systems/gi, '多智能体系统'],
    [/Hallucination-Resistant/gi, '抗幻觉'],
    [/Safety-Critical Settings/gi, '安全关键场景'],
    [/Fractional Order Spiking State Space Models/gi, '分数阶脉冲状态空间模型'],
    [/Long Sequence Learning/gi, '长序列学习'],
    [/Spectral Multimodal Graph Pretraining/gi, '谱域多模态图预训练'],
    [/Multimodal-Attributed Graphs/gi, '多模态属性图'],
    [/Vision-Language-Action Models/gi, '视觉-语言-动作模型'],
    [/Scientific Laboratories/gi, '科学实验室'],
    [/Open-Vocabulary Segmentation/gi, '开放词汇分割'],
    [/Image-Conditional Class Pruning/gi, '图像条件类别剪枝'],
    [/Adversarial Robustness Benchmark/gi, '对抗鲁棒性基准'],
    [/World Models/gi, '世界模型'],
    [/Continuous Control/gi, '连续控制'],
    [/Interpretable OOD Detection/gi, '可解释分布外检测'],
    [/Representation Perturbations/gi, '表征扰动'],
    [/Post-Hoc Falsification Operators/gi, '事后证伪算子'],
    [/Frozen Small Code Models/gi, '冻结小型代码模型'],
    [/Synthetic OOD Generation/gi, '合成式分布外样本生成'],
    [/Robust Refusal/gi, '鲁棒拒答'],
    [/Embodied Question Answering/gi, '具身问答'],
    [/Spatial Localization/gi, '空间定位'],
    [/AI-Generated Image Quality Assessment/gi, 'AI 生成图像质量评估'],
    [/Multi-Scale Two-Stream Vision-Language Alignment/gi, '多尺度双流视觉语言对齐'],
    [/Reverse-Engineering/gi, '逆向解析'],
    [/Tensor Compute Path/gi, '张量计算路径'],
    [/Autonomous Scientific Discovery/gi, '自主科学发现'],
    [/Agent Environment Engineering/gi, 'Agent 环境工程'],
    [/Agent Assessment/gi, 'Agent 评测'],
    [/Openness/gi, '开放性'],
    [/Standardization/gi, '标准化'],
    [/Reproducibility/gi, '可复现性'],
    [/Reliable Spatial Annotations/gi, '可靠空间标注'],
    [/Robot Demonstrations/gi, '机器人示范'],
    [/Content Moderation Feedback System/gi, '内容审核反馈系统'],
    [/Insensitive Speech/gi, '不敏感言论'],
    [/Indigenous Ethnic and Religious Minority Communities/gi, '原住民、少数族裔与宗教少数群体'],
    [/LLM-based/gi, '基于 LLM 的'],
    [/Framework/gi, '框架'],
    [/Platform/gi, '平台'],
    [/Benchmark/gi, '基准'],
    [/Evaluation/gi, '评测'],
    [/Assessment/gi, '评估'],
    [/Agentifying/gi, 'Agent 化'],
    [/Agent/gi, 'Agent'],
    [/Extraction/gi, '抽取'],
    [/Rewriting/gi, '改写'],
    [/Grounding/gi, '落地'],
    [/at Scale/gi, '的大规模方法'],
    [/Using/gi, '使用'],
    [/for/gi, '面向'],
    [/from/gi, '来自'],
    [/toward/gi, '面向'],
    [/and/gi, '与'],
  ];
  for (const [pattern, replacement] of phraseRules) text = text.replace(pattern, replacement);
  return normalizeTitle(text)
    .replace(/\s*:\s*/g, '：')
    .replace(/\s*,\s*/g, '，')
    .replace(/\s+/g, ' ')
    .trim();
}
