class doge:
    bgred='\033[41m'
    black = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'
    lightblue='\033[36m'
    red = '\033[31m'
    bold = '\033[01m'
    reset = '\033[0m'

def col_info(text,defe='\n'):
    print(f"{doge.lightblue}{doge.bold}[Info]{doge.reset}{doge.bold} {text}",end=defe)

def col_exit(text):
    print(f"\n{doge.red}{doge.bold}[Exit] {text}{doge.reset}")

def col_selected(text):
    print(f"\n{doge.yellow}{doge.bold}[Selected] {text}{doge.reset}")
