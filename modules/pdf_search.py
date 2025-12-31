from duckduckgo_search import DDGS

def search_pdfs(n,c):
    q=f'"{n}" "{c}" filetype:pdf'
    a=[]
    with DDGS() as d:
        for r in d.text(q,max_results=25):
            if str(r.get("href","")).endswith(".pdf"):
                a.append(r.get("href"))
    return a