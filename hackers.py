# Import Module
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk

from tkinter import *
from tkinter import messagebox
import requests
import json
from tkinter import filedialog

import webbrowser
from tkinter import END, Text
import tkinter.simpledialog as sd
from tkterminal import Terminal


class home: 
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('1350x700+0+0')
        self.frame1 = tkinter.Label(self.root,width = 400,height = 400,bg = '#AAAAAA')
        self.frame1.pack()
        self.root.title("hackers")
        self.root.geometry('1350x700+0+0')
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='File', menu = file)
        file.add_command(label ='New File', command = home)
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files",".txt"),("all files","*.*")))
            label_file_explorer.configure(text="File Opened: "+filename)
        file.add_command(label ='Open...', command = browseFiles)
        file.add_command(label ='Save', command = None)
        file.add_separator()
        file.add_command(label ='Exit', command = self.root.destroy)
        # Adding Edit Menu and commands
        edit = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
        # Adding Help Menu
        help_ = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Tk Help', command = None)
        help_.add_command(label ='Demo', command = None)
        help_.add_separator()
        help_.add_command(label ='About Tk', command = None)
        
        
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def sql():
            F2 = Frame(self.root, bd=8, relief=GROOVE,bg="#048920")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="sql injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#048920", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
                text_box.pack()
                get_button.pack() 
            def p():
                from sql import Remotephp1
                r = Remotephp1
            def CVE_2022_31101sql():
                from sql import CVE_2022_31101sql
                #CVE_2022_31101sql()
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="SQL Injection : In this section, we'll explain what SQL injection is, describe some common examples, explain how to find \nand exploit various kinds of SQL injection vulnerabilities, and summarize how to prevent SQL injection.\nWhat is SQL injection (SQLi)?\nSQL injection is a web security vulnerability that allows an attacker to \ninterfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to \nretrieve. This might include data belonging to other users, or any other data that the application itself is able to\n access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's\n content or behavior.In some situations, an attacker can escalate an SQL injection \nattack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", 
                                                 relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix",command = p, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                                  relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="CVE-2022-31101sql",command = CVE_2022_31101sql,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                                  relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", 
                                                 relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", 
                                                  relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                                  relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                          relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", 
                                          relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                           relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                            relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE,
                                                            bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",
                                                          relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", 
                                                      relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)
  
           # b6_button = Button(F2, text ="Greenplum", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.80,anchor = NE)#, , , , , , , , , , , H2, HSQLDB, IBM DB2, Informix, InterSystems Cache, Iris, MariaDB, Mckoi, MemSQL, Microsoft Access, Microsoft SQL Server, MimerSQL, MonetDB, MySQL, Oracle, Percona, PostgreSQL, Presto, Raima Database Manager, SAP MaxDB, SQLite, Sybase, TiDB, Vertica, Virtuoso, Yellowbrick, YugabyteDB

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def xss():
            F2 = Frame(self.root, bd=8, relief=GROOVE ,bg="#918713")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xss injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#918713", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
  
                text_box.pack()
                get_button.pack() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="A Cross-Site Scripting (XSS) attack is characterized by an attacker's ability to inject to a web application,\n scripts of any kind, such as Flash, HTML, or JavaScript, \nthat are intended to run and render on the application serving the page. The web application unintentionally serves the\n script code which is executed by the browser and hence makes the user vulnerable to data theft and any privileges level\n which the script is allowed.The source of an XSS vulnerability lies in a web application that allows malicious\n code to be injected and evaluated as part of the web page being served to the user, and then the same malicious\n code is executed by the browser due to the web application inability to filter and sanitize the output.", font=(
            "arial", 12, "bold"), bd=7, relief=GROOVE, bg="#b6ad48", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
        def comment():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#9c6105")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="Command injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#9c6105", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
  
                text_box.pack()
                get_button.pack() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system \nvia a vulnerable application. Command injection attacks are possible when an application \npasses unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell. In this attack,\n the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. \nCommand injection attacks are possible largely due to insufficient input validation.\nThis attack differs from Code Injection, in that code injection allows the attacker to add their own code that is\n then executed by the application. In Command Injection, the attacker extends the default functionality of\n the application, which execute system commands, without the necessity of injecting code.", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#be8f47", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def ssf():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#0c8c6d"  )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="ssf injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#0c8c6d", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="white").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    #quote = data['content']
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
  
                text_box.pack()
                get_button.pack() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="SSIs are directives present on Web applications used to feed an HTML page with dynamic contents. \nThey are similar to CGIs, except that SSIs are used to execute some actions before the current page is\n loaded or while the page is being visualized. In order to do so, the web server analyzes SSI before supplying the\n page to the user. The Server-Side Includes attack allows the exploitation of a web application by injecting scripts in HTML \npages or executing arbitrary codes remotely. It can be exploited through manipulation of SSI \nin use in the application or force its use through user input fields. It is possible to check if the application is properly\n validating input fields data by inserting characters that are used in SSI directives, like:", font=(
            "arial", 12, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="#404040")#.pack(fill=X)
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def profile():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#105392" )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="working", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#105392", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    #quote = data['content']
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
  
                text_box.pack()
                get_button.pack() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#4e88be", fg="#404040")#.pack(fill=X)
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def xml():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#8322a4")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xml injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#8322a4", fg="white").pack(fill=X)
            def Time_Based():
                from xmlin import cope
                F2 = cope() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="In this section, we'll explain what XML external entity injection is, describe some common examples, explain how to find and \nexploit various kinds of XXE injection, and summarize how to prevent XXE injection attacks.\nWhat is XML external entity injection?\nXML external entity injection (also known as XXE) is a web security vulnerability\n that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on\n the application server filesystem, and to interact with any backend or external systems that the application \nitself can access.In some situations, an attacker can escalate an XXE attack to compromise the underlying server or other\n backend infrastructure, by leveraging the XXE vulnerability to perform server-side request forgery (SSRF) attacks.", font=(
            "arial", 12, "bold"), bd=7, relief=GROOVE, bg="#9a65ac", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
            
        def service():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#92147b" )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="denial of service", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#92147b", fg="white").pack(fill=X)
            def Time_Based():
                F2 = Frame(self.root, bd=8, relief=GROOVE)
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="sql injection", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
                def get_quote():
                    r = requests.get('https://hackerone.com/users/sign_in')
                    data = r.text
                    #quote = data['content']
                    text_box.delete('1.0', END)
                    text_box.insert(END, data)  
                text_box = Text(F2, height=10, width=50)
                get_button = Button(F2, text="Get Quote", command=get_quote)
  
                text_box.pack()
                get_button.pack() 
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="In computing, a denial-of-service attack (DoS attack) is a cyber-attack in which \nthe perpetrator seeks to make a machine or network resource unavailable to its intended users by\n temporarily or indefinitely disrupting services of a host connected to a network. Denial of service is typically \naccomplished by flooding the targeted machine or resource with superfluous requests in an attempt to\n overload systems and prevent some or all legitimate requests from being fulfilled. ", font=(
            "arial", 13, "bold"), bd=7, relief=GROOVE, bg="#af559f", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = Time_Based, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="sqlmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE) 

###########################################################################################################

######################################################################################################################################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def injection():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#6e0f03")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="shaw all injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#6e0f03", fg="white").pack(fill=X)
                 
            Hacher_tooles = LabelFrame(F2, text="All Payloads", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)

            def xssinjection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"xss-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
            
            def sqlinjection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"sql-injection-payload-list.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
            
            def commamd_injection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"Command-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
            
            def xml_injection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"xxe-injection-payload-list.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
            
            def ddos():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"dos-doss.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 

            def server_side():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"server-side-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
                

            def Server_side_template():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="#6e0f03")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"Server-side-template.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1)

            def back():
                F3 = injection()
             
            Hacher_s = LabelFrame(F2, text="prat injection", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#6e0f03", fg="#ccc4c4")
            Hacher_s.place(x=2, y=49, relwidth=0.24, relheight=0.92)
            p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
            p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
            b2_button = Button(F2, text ="xss injection",command = xssinjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.15,anchor = NE)
          
            b4_button = Button(F2, text ="sql injection",command = sqlinjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx =0.23, rely = 0.24,anchor = NE)
            

            b5_button = Button(F2, text ="commamd injection",command = commamd_injection,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.33,anchor = NE)
            
  
            b6_button = Button(F2, text ="xml injection",command = xml_injection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.42,anchor = NE)

            b6_button = Button(F2, text ="dos ddos",command = ddos, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.51,anchor = NE)
            
            b2_button = Button(F2, text ="server-side-injection",command = server_side, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.60,anchor = NE)
            
            b2_button = Button(F2, text ="Server-side-template",command = Server_side_template, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.69,anchor = NE)
          
            #b4_button = Button(F2, text ="commix",command = sqlinjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.78,anchor = NE)
            
  
            b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#6e0f03").place(relx = 0.23, rely = 0.90,anchor = NE)
            

####################################################################################

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def CVEPoC():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#105392" )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="All hacks for a year CVE-2023", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#105392", fg="white").pack(fill=X)
            
            Hacher_s = LabelFrame(F2, text="CVE-2023 Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=45, relwidth=0.24, relheight=0.92)
            b2_button = Button(F2, text ="CVE-2023-0861", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)            
  
            b5_button = Button(F2, text ="CVE-2023-1671",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.23,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-1671", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.31,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-2825", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.39,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-2825", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.47,anchor = NE)
          
            b4_button = Button(F2, text ="CVE-2023-2868", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.55,anchor = NE)
            
  
            b5_button = Button(F2, text ="CVE-2023-2877",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.63,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-2982", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.71,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-2986", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.79,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-3460", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.87,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023 poc", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=45, relwidth=0.24, relheight=0.92)

            b2_button = Button(F2, text ="cve-2023-3519", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.15,anchor = NE)
          
            b5_button = Button(F2, text ="cve-2023-10608",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.23,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-20110", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.31,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-20887", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.39,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-21554", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.47,anchor = NE)
          
            b4_button = Button(F2, text ="CVE-2023-21707", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.55,anchor = NE)
            
  
            b5_button = Button(F2, text ="CVE-2023-21716",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.63,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-21716", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.71,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-21837", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.79,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-21839", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.87,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=45, relwidth=0.24, relheight=0.92)

            b2_button = Button(F2, text ="CVE-2023-22621", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.15,anchor = NE)
          
            b5_button = Button(F2, text ="CVE-2023-22809",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.23,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-22884", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.31,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-22906", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.39,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-22960", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.47,anchor = NE)
          
            b4_button = Button(F2, text ="CVE-2023-23333", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.55,anchor = NE)
            
  
            b5_button = Button(F2, text ="CVE-2023-23397",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.63,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-23488", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.71,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-23752", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.79,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-24078", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.87,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=45, relwidth=0.24, relheight=0.92)

            b2_button = Button(F2, text ="CVE-2023-24488", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.15,anchor = NE)
          
            b5_button = Button(F2, text ="CVE-2023-24489",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.23,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-24775", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.31,anchor = NE)
            b6_button = Button(F2, text ="CVE-2023-25136", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.39,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-27163", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.47,anchor = NE)
          
            b4_button = Button(F2, text ="CVE-2023-27350", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.55,anchor = NE)
            
  
            b5_button = Button(F2, text ="CVE-2023-27372",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.63,anchor = NE)
            
  
            b6_button = Button(F2, text ="CVE-2023-27524", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.71,anchor = NE)
            b6_button = Button(F2, text ="cve-2022-42475", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.79,anchor = NE)
            
            b2_button = Button(F2, text ="CVE-2023-28771", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.87,anchor = NE)
            

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

######################################################################################################################################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        F1 = LabelFrame(self.root, text="Tooles", font=(
            "times new roman", 15, "bold"),  bd=12, relief=GROOVE, bg="#404040",fg = "white")
        F1.place(x=7, y=70, width=300, relheight=0.84)
        
        def main():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#679a80")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="working", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").pack(fill=X)
       

       
       
############################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
            def sqlmap():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#d89239"  )
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="work apron sqlmap", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#ba6a04", fg="black").pack(fill=X)
                Hacher_des = Label(F2, text="sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking \nover of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of \nswitches including database fingerprinting, over data fetching from the database, accessing the underlying file system,\n and executing commands on the operating system via out-of-band connections.", font=(
                "arial", 10, "bold"), bd=7, relief=GROOVE, bg="white", fg="#404040").pack(fill=X)

                Hacher_part = LabelFrame(F2, text="commands sqlmap", font=(
                "arial", 10, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                Hacher_part.place(x=2, y=130, relwidth=0.26, relheight=0.77)
                p_part = Label(F2, text="Here is the workspace where commands are entered", font=(
                "arial", 15, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p_part.place(relx = 0.63, rely = 0.30, relwidth=0.73,anchor = 's')
                terminal = Terminal(pady=2, padx=2, relief=GROOVE, bg="#404040",fg = "white")
                terminal.shell = True
                terminal.place(x=580, y=256, relwidth=0.54, relheight=0.55)
                '''
                def printInput():
                    inp = inputtxt.get(1.0, "end-1c")
                    lbl.config(text = inp)
                inputtxt = tk.Text(F2,
                         height = 5,
                          width = 20)
  
                inputtxt.place(relx = 0.23, rely = 0.50,anchor = NE)
  

                printButton = tk.Button(F2,
                        text = "Print", 
                        command = printInput)
                printButton.place(relx = 0.23, rely = 0.66,anchor = NE)
  

                lbl = tk.Label(F2, text = "")
                lbl.place(relx = 0.23, rely = 0.80,anchor = NE)
                '''
                p = Label(F2, text="Download sqlmap by clicking", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.27,anchor = NE)

                b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'pip install sqlmap ', 'y')).place(relx = 0.23, rely = 0.32,anchor = 's')

                p = Label(F2, text="To get a list of all options and\nswitches clicking:", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.31,anchor = NE)

                b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'sqlmap -hh', 'y')).place(relx = 0.23, rely = 0.38,anchor = 's')

                pat = Label(F2, text="Target URL. Option: -u or --url\nRun sqlmap against a single target URL.\n This option requires a target\nURL in following form:\nhttp(s)://targeturl[:port]/[...]\nFor example:", font=(
                       "arial", 9, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.54,anchor = 's')

                pat1 = Label(F2, text="$sqlmap -u 'http://www.target.com/vuln.php?id=1'", font=(
                       "arial", 7, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.56,anchor = 's')

                p2 = Label(F2, text="to run simple sqlmap", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.16, rely = 0.59,anchor = NE)
                p3 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'sqlmap --wizard', 'y')).place(relx = 0.23, rely = 0.63,anchor = 's')
                def callback(url):
                    webbrowser.open_new(url)
                link1 = Label(F2, text="for further use.", fg="blue", cursor="hand2")
                link1.place(relx = 0.13, rely = 0.67,anchor = 's')
                link1.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/wiki/Usage"))

                link2 = Label(F2, text="to visit the home page", fg="blue", cursor="hand2")
                link2.place(relx = 0.13, rely = 0.73,anchor = 's')
                link2.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/"))

               
            def commix():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#d89239"  )
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="work apron commix", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#ba6a04", fg="black").pack(fill=X)
                Hacher_des = Label(F2, text="Automated All-in-One OS Command Injection Exploitation ToolCommix \n(short for [comm]and [i]njection e[x]ploiter) is an open source penetration testing tool, written by Anastasios Stasinopoulos\n, that automates the detection and exploitation of command injection vulnerabilities.",   font=("arial", 10, "bold"), bd=7, relief=GROOVE, bg="white", fg="#404040").pack(fill=X)

                Hacher_part = LabelFrame(F2, text="commands commix", font=(
                "arial", 10, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                Hacher_part.place(x=2, y=130, relwidth=0.26, relheight=0.77)
                p_part = Label(F2, text="Here is the workspace where commands are entered", font=(
                "arial", 15, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p_part.place(relx = 0.63, rely = 0.30, relwidth=0.73,anchor = 's')
                terminal = Terminal(pady=2, padx=2, relief=GROOVE, bg="#404040",fg = "white")
                terminal.shell = True
                terminal.place(x=580, y=256, relwidth=0.54, relheight=0.55)
                p = Label(F2, text="Download commix by clicking", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.27,anchor = NE)

                b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'pip install commix ', 'y')).place(relx = 0.23, rely = 0.32,anchor = 's')

                p = Label(F2, text="To get a list of all options and\nswitches clicking:", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.31,anchor = NE)

                b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'commix -hh', 'y')).place(relx = 0.23, rely = 0.38,anchor = 's')

                pat = Label(F2, text="Target URL. Option: -u or --url\nRun commix against a single target URL.\n This option requires a target\nURL in following form:\nhttp(s)://targeturl[:port]/[...]\nFor example:", font=(
                       "arial", 9, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.54,anchor = 's')

                pat1 = Label(F2, text="$commix -u 'http://www.target.com/vuln.php?id=1'", font=(
                       "arial", 7, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.56,anchor = 's')

                p2 = Label(F2, text="to run simple commix", font=(
                       "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.16, rely = 0.59,anchor = NE)
                p3 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",
                    command=lambda: terminal.run_command(f'commix --wizard', 'y')).place(relx = 0.23, rely = 0.63,anchor = 's')
                def callback(url):
                    webbrowser.open_new(url)
                link1 = Label(F2, text="for further use.", fg="blue", cursor="hand2")
                link1.place(relx = 0.13, rely = 0.67,anchor = 's')
                link1.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/wiki/Usage"))

                link2 = Label(F2, text="to visit the home page", fg="blue", cursor="hand2")
                link2.place(relx = 0.13, rely = 0.73,anchor = 's')
                link2.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/"))

                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#679a80", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = sqlmap, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix",command =commix, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="beef",fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="dotdotpwn", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="abuse-ssl-bypass-waf", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="jok3r", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="nmap", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="joomscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wpscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="httpx", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="log4j-scan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="magescan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Fuzzer", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="conscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="crlf-injector", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="wfuzz", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="dirb", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="amass", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="nikto", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles get", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            b2_button = Button(F2, text ="cewl", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="gooscan", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            b5_button = Button(F2, text ="sn1per", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            b6_button = Button(F2, text ="backdoorppt", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
            b6_button = Button(F2, text ="wsfuzzer", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            b2_button = Button(F2, text ="sublist3r", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
        F2 = main()

        self.btn = Button(self.root, text = "sql injection",command=sql, width=20, bd=7, font=("arial 15 bold", 15, "bold"), relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid
        self.btn.place(relx = 0.21, rely = 0.14,anchor = NE)
# inside
        self.btn = Button(self.root, text = "xss injection",command=xss, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid
        self.btn.place(relx = 0.21, rely = 0.22,anchor = NE)
# inside
        self.btn = Button(self.root, text = "Command injection",command=comment, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid

        self.btn.place(relx = 0.21, rely = 0.30,anchor = NE)
# inside
        self.btn = Button(self.root, text = "ssf injection",command=ssf, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid

        self.btn.place(relx = 0.21, rely = 0.38,anchor = NE)
        self.btn1 = Button(self.root, text = 'xml injection',command = xml, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.46,anchor = NE)
        self.btn1 = Button(self.root, text = 'denial of service',command = service, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.54,anchor = NE)
        self.btn1 = Button(self.root, text = 'show injection',command = injection, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.62,anchor = NE)
        self.btn1 = Button(self.root, text = 'CVE-2023-PoC',command = CVEPoC, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.70,anchor = NE)
        self.btn1 = Button(self.root, text = 'Back to the tools',command = main, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
        self.btn1.place(relx = 0.21, rely = 0.78,anchor = NE)
        self.btn1 = Button(self.root, text = 'Quit !',command = self.root.destroy, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="red")
        self.btn1.place(relx = 0.21, rely = 0.85,anchor = NE)

        
        title = Label(self.root, text="Hackers A Tooles", font=("times new roman", 20, "bold"),
                      pady=2, bd=12, width=100, relief=GROOVE, bg="#404040", fg="#ccc4c4")
        title.place(relx = 0.5, rely = 0.1,anchor = 's')
        self.root.resizable(True, True)
    #create menu
###########################################################################################################

###########################################################################################################
    
    def popup(self):
        self.popup_menu = tkinter.Menu(self.root,
                                       tearoff = 0)
          
        self.popup_menu.add_command(label = "say hi",
                                    command = lambda:self.hey("hi"))
          
        self.popup_menu.add_command(label = "say hello",
                                    command = lambda:self.hey("hello"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "say bye",
                                    command = lambda:self.hey("bye"))
   
    #display menu on right click
    def do_popup(self,event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()
   
    def hey(self,s):
        self.frame1.configure(text = s)
          
    def run(self):
        self.popup()
        self.root.bind("<Button-3>",self.do_popup)
        tkinter.mainloop()
    
  
a = home()
a.run()
