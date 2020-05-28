#!/usr/bin/env python

import re
import requests
from time import sleep
from downloader import downloader


def filter_data(url):
    print("[+]\tFiltering data on: " + url)

    try:
        response = requests.get(url)
        sleep(1)
        content = response.text

        if response.status_code == 200:
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?\|.*', content):
                print("[+]\t Downloading " + url + ". a email with password was found on the page")
                downloader(url, content)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?:.*', content):
                print("[+]\t Downloading " + url + ". a email with password was found on the page")
                downloader(url, content)
                return

            if re.search(r'pridesec\.com\.br|pridesec', content):
                print("[+]\t Downloading " + url + ". a mention to pridesec was found on the page")
                downloader(url, content)
                return

            if re.search(r'-----BEGIN (RSA|DSA) PRIVATE KEY-----', content):
                print("[+]\t Downloading " + url + ". a RSA or DSA private key was found on the page")
                downloader(url, content)
                return

            if re.search(r'\-\-[pP]assword\=[^%^\$]', content):
                print("[+]\t Downloading " + url + ". a --password= was found on the page")
                downloader(url, content)
                return

            if re.search(r'\-\-[sS]enha\=[^%^\$]', content):
                print("[+]\t Downloading " + url + ". a --senha= was found on the page")
                downloader(url, content)
                return

            if re.search(r'[hH][aA4][cC][kK][eE3][dD]  [bB][yY]', content):
                print("[+]\t Downloading " + url + ". a hacked by was found on the page")
                downloader(url, content)
                return

    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        pass
    except requests.HTTPError:
        pass
