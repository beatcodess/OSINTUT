from duckduckgo_search import DDGS
from PIL import Image
import requests, io, hashlib

def _phash(b):
    img=Image.open(io.BytesIO(b)).resize((8,8)).convert("L")
    px=list(img.getdata())
    avg=sum(px)/64
    return "".join("1" if p>avg else "0" for p in px)

def _exif(img):
    try:
        return {Image.ExifTags.TAGS.get(k):v for k,v in img._getexif().items()}
    except:
        return {}

def search_images(n,c):
    q=f'"{n}" "{c}"'
    out=[]
    with DDGS() as d:
        for r in d.images(q,max_results=30):
            url=r.get("image")
            if not url: continue
            try:
                b=requests.get(url,timeout=6).content
                img=Image.open(io.BytesIO(b))
            except:
                continue
            out.append({
                "url":url,
                "hash":_phash(b),
                "exif":_exif(img)
            })
    return out
