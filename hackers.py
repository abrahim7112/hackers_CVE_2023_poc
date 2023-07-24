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

        def sql():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="sql injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
             

            b1_button = Button(F2, text ="Apache Ignite", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.70,anchor = NE)
            
  
            b2_button = Button(F2, text ="Aurora", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.80,anchor = NE)
  
            b3_button = Button(F2, text ="ClickHouse", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.90,anchor = NE)
  
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)
  
            b6_button = Button(F2, text ="Greenplum", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.80,anchor = NE)#, , , , , , , , , , , H2, HSQLDB, IBM DB2, Informix, InterSystems Cache, Iris, MariaDB, Mckoi, MemSQL, Microsoft Access, Microsoft SQL Server, MimerSQL, MonetDB, MySQL, Oracle, Percona, PostgreSQL, Presto, Raima Database Manager, SAP MaxDB, SQLite, Sybase, TiDB, Vertica, Virtuoso, Yellowbrick, YugabyteDB
            b3_button = Button(F2, text ="MySQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.90,anchor = NE)
            
            b1_button = Button(F2, text ="Altibase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.82, rely = 0.30,anchor = NE)
            b5_button = Button(F2, text ="CrateDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.82, rely = 0.40,anchor = NE)
            b1_button = Button(F2, text ="Drizzle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.82, rely = 0.50,anchor = NE)
            b4_button = Button(F2, text ="CockroachDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.82, rely = 0.60,anchor = NE)

###########################################################################################################

###########################################################################################################


        def xss():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xss injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)

###########################################################################################################

###########################################################################################################

        def comment():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="Command injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def ssf():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="ssf injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)

###########################################################################################################

###########################################################################################################

        def profile():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="working", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)

###########################################################################################################

###########################################################################################################

        def xml():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xml injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)

###########################################################################################################

###########################################################################################################
            
        def service():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="denial of service", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE) 

###########################################################################################################

###########################################################################################################


        def injection():
            F2 = Frame(self.root, bd=8, relief=GROOVE)
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="all injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="yellow", fg="black").pack(fill=X)
            b2_button = Button(F2, text ="Amazon Redshift", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.30,anchor = NE)
          
            b4_button = Button(F2, text ="Apache Derby", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.40,anchor = NE)
            
  
            b5_button = Button(F2, text ="PostgreSQL", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.50,anchor = NE)
            
  
            b6_button = Button(F2, text ="Oracle", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.28, rely = 0.60,anchor = NE)
            b6_button = Button(F2, text ="Cubrid", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.30,anchor = NE)
            
            b2_button = Button(F2, text ="EnterpriseDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.40,anchor = NE)
  
            b3_button = Button(F2, text ="eXtremeDB", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.50,anchor = NE)
  
            b4_button = Button(F2, text ="Firebird", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.60,anchor = NE)
  
            b5_button = Button(F2, text ="FrontBase", fg ="black",width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="brown").place(relx = 0.55, rely = 0.70,anchor = NE)


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

        F1 = LabelFrame(self.root, text="Tooles", font=(
            "times new roman", 15, "bold"),  bd=12, relief=GROOVE, bg="#404040",fg = "white")
        F1.place(x=7, y=70, width=300, relheight=0.84)
        F2 = Frame(self.root, bd=8, relief=GROOVE)
        F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
        Hacher_title = Label(F2, text="working", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").pack(fill=X)
        scroll_y = Scrollbar(F2, orient=VERTICAL)
        self.txtarea = Text(F2, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.insert(
            END, "Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!!")
        self.txtarea.pack(fill=BOTH, expand=1)

###########################################################################################################

###########################################################################################################

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

        self.btn.place(relx = 0.21, rely = 0.29,anchor = NE)
# inside
        self.btn = Button(self.root, text = "ssf injection",command=ssf, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid

        self.btn.place(relx = 0.21, rely = 0.37,anchor = NE)
        self.btn1 = Button(self.root, text = 'xml injection',command = xml, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.45,anchor = NE)
        self.btn1 = Button(self.root, text = 'denial of service',command = service, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.53,anchor = NE)
        self.btn1 = Button(self.root, text = 'show injection',command = injection, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.61,anchor = NE)
        self.btn1 = Button(self.root, text = 'show injection',command = show, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.69,anchor = NE)
        self.btn1 = Button(self.root, text = 'profile',command = profile, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.77,anchor = NE)
        self.btn1 = Button(self.root, text = 'Quit !',command = self.root.destroy, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="red", fg="#ccc4c4")
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
