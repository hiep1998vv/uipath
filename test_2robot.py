import requests
import os
from getmac import get_mac_address as gma
import socket
import json
import psutil
import time

hostname = socket.gethostname()
IPAdr = socket.gethostbyname(hostname)

print(hostname)
print(IPAdr)
print(gma())
def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)
while True:
    url ="http://192.168.173.17/Api/RPA/get_rpa_start?pcmac="+gma()+"&Status=Start"
    response = requests.get(url, timeout =1000).text
    print(response)
    if (response == []):
        continue
    else:
        # kill process cua robot truoc
        kill_by_process_name_shell("UiPath.Executor.exe")

        # run robot
        path = json.loads(response)[0]["BatFile"]
        print(path)
        os.system(path)


