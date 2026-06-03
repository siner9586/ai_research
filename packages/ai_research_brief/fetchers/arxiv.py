from datetime import datetime, timezone
from urllib.parse import quote
import feedparser
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed
from ..models import Paper

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def fetch_arxiv_category(category: str, max_results: int = 50) -> list[Paper]:
    query = quote(f'cat:{category}')
    url = f'https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={max_results}'
    r = httpx.get(url, timeout=30, headers={'User-Agent':'ai-research-brief/0.1'})
    r.raise_for_status()
    feed = feedparser.parse(r.text)
    papers = []
    for e in feed.entries:
        arxiv_id = e.id.split('/abs/')[-1]
        cats = [t['term'] for t in getattr(e, 'tags', [])]
        papers.append(Paper(id=arxiv_id, arxiv_id=arxiv_id, title=e.title.replace('\n',' ').strip(), abstract=e.summary.replace('\n',' ').strip(), authors=[a.name for a in getattr(e,'authors',[])], primary_category=cats[0] if cats else category, categories=cats or [category], published_at=datetime(*e.published_parsed[:6], tzinfo=timezone.utc), updated_at=datetime(*e.updated_parsed[:6], tzinfo=timezone.utc), abs_url=e.id, pdf_url=e.id.replace('/abs/','/pdf/')))
    return papers

def mock_papers() -> list[Paper]:
    now = datetime.now(timezone.utc)
    rows = [
        ('2606.00001','Self Evolving Agents for Tool Use Skills','Agents learn tool use skills through iterative self improvement and evaluation.',['Alice Chen','Bob Smith'],'cs.AI'),
        ('2606.00002','Efficient Long Context Inference with Cache Compression','A systems method for reducing memory during long context model inference.',['Carol Li'],'cs.LG'),
        ('2606.00003','RAG Evaluation under Noisy Retrieval','A benchmark studies retrieval augmented generation reliability under noisy evidence.',['Dan Wang'],'cs.IR'),
        ('2606.00004','Multimodal Safety Evaluation for Vision Language Models','A safety evaluation suite for multimodal models across risky visual prompts.',['Eva Green'],'cs.CV'),
        ('2606.00005','Code Model Repair with Execution Feedback','Code models improve patch generation through execution feedback loops.',['Frank Moore'],'cs.CL'),
    ]
    return [Paper(id=i, arxiv_id=i, title=t, abstract=a, authors=au, primary_category=c, categories=[c], published_at=now, updated_at=now, abs_url=f'https://arxiv.org/abs/{i}', pdf_url=f'https://arxiv.org/pdf/{i}') for i,t,a,au,c in rows]
