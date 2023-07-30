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
    
    #creates parent window
    def __init__(self):
        
            
        self.root = tkinter.Tk()
        self.root.geometry('1350x700+0+0')
   
        self.frame1 = tkinter.Label(self.root,
                                    width = 400,
                                    height = 400,
                                    bg = '#AAAAAA')
        self.frame1.pack()
        self.root.title("hackers")
# Set geometry(widthxheight)
        self.root.geometry('1350x700+0+0')
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='File', menu = file)
        file.add_command(label ='New File', command = home)
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files",".txt"),("all files","*.*")))
	
	# Change label contents
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
        #help.add_command(label='About')
        
        
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
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="#404040")#.pack(fill=X)
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
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#918713", fg="black").pack(fill=X)
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
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#b6ad48", fg="#404040")#.pack(fill=X)
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
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#be8f47", fg="#404040")#.pack(fill=X)
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
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="#404040")#.pack(fill=X)
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
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#9a65ac", fg="#404040")#.pack(fill=X)
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
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#af559f", fg="#404040")#.pack(fill=X)
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
            Hacher_title = Label(F2, text="all injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#6e0f03", fg="black").pack(fill=X)
            

  
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
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#9d5047", fg="#404040")#.pack(fill=X)
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


        def show():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="Doc", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            Hacher_doc = Label(F2, text="Doc", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, fg="black").pack(fill=X)
            treeview = ttk.Treeview(F2) 
            treeview.place(x=2, y=23,relwidth=0.20, relheight=0.85,relx = 0.20, rely = 0.10,anchor = NE) 
            treeview.insert('', '0', 'item1',text ='sql injection')
            treeview.insert('', '1', 'item2',text ='Computer Science')
            treeview.insert('', '2', 'item3',text ='GATE papers')
            treeview.insert('', 'end', 'item4',text ='Programming Languages')
            treeview.insert('item2', 'end', 'Algorithm',text ='Algorithm') 
            treeview.insert('item2', 'end', 'Data structure',text ='Data structure')
            treeview.insert('item3', 'end', '2018 paper',text ='2018 paper') 
            treeview.insert('item3', 'end', '2019 paper',text ='2019 paper')
            treeview.insert('item4', 'end', 'Python',text ='Python')
            treeview.insert('item4', 'end', 'Java',text ='Java')
            treeview.move('item2', 'item1', 'end') 
            treeview.move('item3', 'item1', 'end')
            treeview.move('item4', 'item1', 'end')
            
            treeview.insert('', '0', 'item1',text ='sql injection')
            treeview.insert('', '1', 'item2',text ='Computer Science')
            treeview.insert('', '2', 'item3',text ='GATE papers')
            treeview.insert('', 'end', 'item4',text ='Programming Languages')
            treeview.insert('item2', 'end', 'Algorithm',text ='Algorithm') 
            treeview.insert('item2', 'end', 'Data structure',text ='Data structure')
            treeview.insert('item3', 'end', '2018 paper',text ='2018 paper') 
            treeview.insert('item3', 'end', '2019 paper',text ='2019 paper')
            treeview.insert('item4', 'end', 'Python',text ='Python')
            treeview.insert('item4', 'end', 'Java',text ='Java')
            treeview.move('item2', 'item1', 'end') 
            treeview.move('item3', 'item1', 'end')
            treeview.move('item4', 'item1', 'end')
            

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
       # scroll_y = Scrollbar(F2, orient=VERTICAL)
        #self.txtarea = Text(F2, yscrollcommand=scroll_y.set, font=(
         #   "times new roman", 15, "bold"), fg="#3206b8")
        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_y.config(command=self.txtarea.yview)
        #self.txtarea.insert(
        #    END, "Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!!")
       # self.txtarea.pack(fill=BOTH, expand=1)
        
        #Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
         #   "arial", 10, "bold"), bd=7, relief=GROOVE, bg="white", fg="#404040").pack(fill=X)

        #Hacher_tooles = Label(F2, text="Tooles Other", font=(
         #   "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").pack(fill=X)
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
  
# Button Creation
                printButton = tk.Button(F2,
                        text = "Print", 
                        command = printInput)
                printButton.place(relx = 0.23, rely = 0.66,anchor = NE)
  
# Label Creation
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

                #root.mainloop()
            def Time_Based():
                # prompts message on screen and gets the command
                value = 'sqlmap -h'
                # executes the command and returns
                # the output in stream variable
                stream = os.popen(value)
                # reads the output from stream variable
                out = stream.read()
                pyautogui.alert(out)
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#679a80", fg="#404040")#.pack(fill=X)
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            b2_button = Button(F2, text ="sqlmap",command = sqlmap, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            b4_button = Button(F2, text ="commix", fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
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
        self.btn1 = Button(self.root, text = 'CVE-2023-PoC',command = show, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

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
