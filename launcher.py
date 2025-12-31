import sys,subprocess,os,importlib.util

REQUIRED=[
    "aiohttp",
    "tk"
]

def install(pkg):
    subprocess.check_call([sys.executable,"-m","pip","install",pkg])

def check_libs():
    for lib in REQUIRED:
        try:
            importlib.import_module(lib)
        except:
            install(lib)

def python_check():
    if sys.version_info < (3,9):
        print("Python 3.9+ required")
        sys.exit(1)

def run_app():
    if not os.path.exists("app.py"):
        print("app.py not found")
        sys.exit(1)
    subprocess.Popen([sys.executable,"app.py"])

if __name__=="__main__":
    python_check()
    check_libs()
    run_app()
