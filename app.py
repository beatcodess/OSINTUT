import tkinter as tk
from tkinter import ttk
import threading,webbrowser

try:
    from modules import username_search
except:
    username_search=None

root=tk.Tk()
root.title("beatcodes")
root.geometry("1000x650")

def open_link(e):
    webbrowser.open("https://guns.lol/beatcodes")

title=tk.Label(root,text="beatcodes",fg="#4da6ff",font=("Segoe UI",18,"bold"),cursor="hand2")
title.pack(pady=6)
title.bind("<Button-1>",open_link)

notebook=ttk.Notebook(root)
notebook.pack(expand=True,fill="both")

def make_tab(name):
    f=ttk.Frame(notebook)
    notebook.add(f,text=name)
    return f

username_tab=make_tab("Username")
name_tab=make_tab("Name")
image_tab=make_tab("Images")
pdf_tab=make_tab("PDFs")
mentions_tab=make_tab("Mentions")
output_tab=make_tab("Output")

output=tk.Text(output_tab,wrap="word")
output.pack(expand=True,fill="both")

def log(t):
    output.insert(tk.END,t+"\n")
    output.see(tk.END)

username_frame=ttk.Frame(username_tab)
username_frame.pack(pady=20)

ttk.Label(username_frame,text="Username").grid(row=0,column=0,padx=6)
username_entry=ttk.Entry(username_frame,width=30)
username_entry.grid(row=0,column=1,padx=6)

use_tor_var=tk.BooleanVar(value=False)
tor_toggle=ttk.Checkbutton(username_frame,text="Use Tor Routing",variable=use_tor_var)
tor_toggle.grid(row=0,column=2,padx=10)

def run_username():
    output.delete("1.0",tk.END)
    u=username_entry.get().strip()
    if not u:
        return
    log("Running username OSINT scan...")
    if not username_search:
        log("username_search module not found")
        return
    r=username_search.find_socials(u,tor=use_tor_var.get())
    for site,data in r.items():
        log(f"[{site}] confidence={data['weight']}")
        for url in set(data["urls"]):
            log("  "+url)
        log("")
    log("Done.")

ttk.Button(username_tab,text="Run Username Scan",command=lambda:threading.Thread(target=run_username,daemon=True).start()).pack(pady=10)

def placeholder(tab,name):
    f=ttk.Frame(tab)
    f.pack(pady=40)
    ttk.Label(f,text=f"{name} module connected").pack()
    ttk.Button(f,text="Run",command=lambda:log(f"{name} scan not implemented in this build")).pack(pady=6)

placeholder(name_tab,"Name")
placeholder(image_tab,"Image")
placeholder(pdf_tab,"PDF")
placeholder(mentions_tab,"Mentions")

root.mainloop()
