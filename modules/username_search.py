import requests,difflib

sites={
"Twitter":"https://twitter.com/{}",
"Instagram":"https://instagram.com/{}",
"GitHub":"https://github.com/{}",
"Reddit":"https://reddit.com/user/{}",
"TikTok":"https://tiktok.com/@{}"
}

def find_socials(u,p):
    r={}
    px={"http":p,"https":p} if p else None
    for k,v in sites.items():
        try:
            x=requests.get(v.format(u),timeout=5,proxies=px)
            if x.status_code==200:
                r[k]=v.format(u)
        except:
            pass
    return r

def alias_score(u,s):
    a={}
    for k,v in s.items():
        a[k]=round(difflib.SequenceMatcher(None,u,u).ratio(),2)
    return a