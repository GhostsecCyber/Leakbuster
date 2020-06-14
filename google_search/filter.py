#!/usr/bin/env python

import requests
from time import sleep
from google_search.filterV2 import *


def filter_data(url):


    try:
        response = requests.get(url)
        sleep(1)
        content = response.text

        if response.status_code == 200:
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?\|.*', content):
                filter_module(url, content)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?;.*', content):
                filter_dot_comma(url, content)
                return

            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?:.*', content):
                filter_two_dots(url, content)
                return

            if re.search(r'pridesec\.com\.br|pridesec', content):
                download_raw_content(url, content)
                return

            if re.search(r'-----BEGIN (RSA|DSA) PRIVATE KEY-----', content):
                download_raw_content(url, content)
                return

            if re.search(r'\-\-[pP]assword\=[^%^\$]', content):
                download_raw_content(url, content)
                return

            if re.search(r'\-\-[sS]enha\=[^%^\$]', content):
                download_raw_content(url, content)
                return
            
            if re.search(r'[hH][aA4][cC][kK][eE3][dD]  [bB][yY]', content):
                download_raw_content(url, content)
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

