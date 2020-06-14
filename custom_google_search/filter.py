#!/usr/bin/env python

import requests
from time import sleep
from custom_google_search.filterV2 import *
from custom_google_search.save_results import save_raw_content


def filter_data(url):

    try:
        response = requests.get(url)
        sleep(1)
        content = response.text

        if response.status_code == 200:
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?\|.*', content):
                if re.search(r'pastebin', url):
                    filter_module(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?;.*', content):
                if re.search(r'pastebin', url):
                    filter_dot_comma(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?:.*', content):
                if re.search(r'pastebin', url):
                    filter_two_dots(url, content)
                else:
                    file = url.split('//')[1]
                    file = file.split('.')[0]
                    save_raw_content(file, content)
                return

            if re.search(r'pridesec\.com\.br|pridesec', content):
                if re.search(r'pastebin', url):
                    download_raw_content(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'-----BEGIN (RSA|DSA) PRIVATE KEY-----', content):
                if re.search(r'pastebin', url):
                    download_raw_content(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'\-\-[pP]assword\=[^%^\$]', content):
                if re.search(r'pastebin', url):
                    download_raw_content(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'\-\-[sS]enha\=[^%^\$]', content):
                if re.search(r'pastebin', url):
                    download_raw_content(url, content)
                else:
                    save_raw_content(url, content)
                return

            if re.search(r'[hH][aA4][cC][kK][eE3][dD]  [bB][yY]', content):
                if re.search(r'pastebin', url):
                    download_raw_content(url, content)
                else:
                    save_raw_content(url, content)
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

