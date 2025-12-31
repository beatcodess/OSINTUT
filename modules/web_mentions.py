from duckduckgo_search import DDGS
from datetime import datetime

def search_mentions(n,c,u):
    q=f'"{n}" "{c}" OR "{u}"'
    a=[]
    with DDGS() as d:
        for r in d.text(q,max_results=30):
            a.append({"title":r.get("title"),"url":r.get("href"),"time":str(datetime.utcnow())})
    return a

def timeline(m):
    return sorted(m,key=lambda x:x["time"])