#!/usr/bin/env python

import re
import requests
from time import sleep
from filterV2 import *


def filter_data(url, csv):
    print("\n[+]\tFiltering data on: " + url)

    try:
        response = requests.get(url)
        sleep(1)
        content = response.text

        if response.status_code == 200:
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?\|.*', content):
                print("[+]\t\t Downloading " + url + ". An email|password was found on the page.")
                filter_module(url, content, csv)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?;.*', content):
                print("[+]\t\t Downloading " + url + ". An email;password was found on the page.")
                filter_dot_comma(url, content, csv)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?:.*', content):
                print("[+]\t\t Downloading " + url + ". An email:password was found on the page.")
                filter_two_dots(url, content, csv)
                return

            if re.search(r'pridesec\.com\.br|pridesec', content):
                print("[+]\t\t Downloading " + url + ". A mention to pridesec was found on the page.")
                download_raw_content(url, content, csv)
                return

            if re.search(r'-----BEGIN (RSA|DSA) PRIVATE KEY-----', content):
                print("[+]\t\t Downloading " + url + ". A RSA or DSA private key was found on the page.")
                download_raw_content(url, content, csv)
                return

            if re.search(r'\-\-[pP]assword\=[^%^\$]', content):
                print("[+]\t\t Downloading " + url + ". A --password= was found on the page.")
                download_raw_content(url, content, csv)
                return

            if re.search(r'\-\-[sS]enha\=[^%^\$]', content):
                print("[+]\t\t Downloading " + url + ". A --senha= was found on the page.")
                download_raw_content(url, content, csv)
                return
            
            if re.search(r'[hH][aA4][cC][kK][eE3][dD]  [bB][yY]', content):
                print("[+]\t\t Downloading " + url + ". A \"hacked by\" was found on the page.")
                download_raw_content(url, content, csv)
                return
            else:
                print("[-]\t\tNothing was found on the page.")

    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        exit()
    except requests.HTTPError:
        pass

