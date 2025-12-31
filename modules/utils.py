import json,os,importlib
from jinja2 import Template
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def save_report(d):
    os.makedirs("output",exist_ok=True)
    with open("output/report.json","w",encoding="utf-8") as f:
        json.dump(d,f,indent=2)

def html_report():
    with open("output/report.json") as f:
        d=json.load(f)
    t=Template("<html><body><pre>{{data}}</pre></body></html>")
    with open("output/report.html","w") as f:
        f.write(t.render(data=json.dumps(d,indent=2)))

def pdf_report():
    with open("output/report.json") as f:
        d=json.load(f)
    doc=SimpleDocTemplate("output/report.pdf")
    styles=getSampleStyleSheet()
    flow=[Paragraph("<pre>"+json.dumps(d,indent=2)+"</pre>",styles["Normal"])]
    doc.build(flow)

def load_plugins(d):
    if not os.path.isdir("plugins"):
        return
    for p in os.listdir("plugins"):
        if p.endswith(".py"):
            m=importlib.import_module("plugins."+p[:-3])
            if hasattr(m,"run"):
                m.run(d)