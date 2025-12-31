from duckduckgo_search import DDGS

def search_images(n,c):
    q=f'"{n}" "{c}"'
    a=[]
    with DDGS() as d:
        for r in d.images(q,max_results=25):
            a.append(r.get("image"))
    return a