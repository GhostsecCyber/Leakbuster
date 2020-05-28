#!/usr/bin/env python

import argparse as arg
import re
from time import sleep
from filter import filter_data

try:
    from googlesearch import search
except ImportError:
    print(
        "No module named 'google' found. Try run the following commands: pip install beautifulsoup4 and pip install google")

print("\n[+]Search on google via terminal created by th3r4ven\n")


def get_arguments(tld):

    # Function responsible for handling arguments,
    # here you can create, delete and modify all arguments using by this program

    opt = arg.ArgumentParser()
    opt.add_argument("-s", "--search", dest="search",
                     help="Query to search on google. E.g: +@gmail.com site:pastebin.com")
    opt.add_argument("-d", dest="domain", help="Top level domain. Use -tld to se all the Top domain level.")

    opt.add_argument("--tld", action="store_true", help="Show e.g. on top level domain. Eg: br: google.com.br.")

    opt.add_argument("-l", "--lang", dest="lang", help="Google search language, E.g.: pt-br, en, es.")
    opt.add_argument("-t", dest="time", help="Time limit to filter the search, use --tbs for more info.")
    opt.add_argument("-min", dest="min", help="Time limit to filter the search, use --tbs for more info.")
    opt.add_argument("-max", dest="max", help="Time limit to filter the search, use --tbs for more info.")

    opt.add_argument("--tbs", action="store_true", help="Show e.g. on time search filter.")
    opt.add_argument("--safe", action="store_true", help=" Activate safe search.")

    opt.add_argument("-n", "--number", dest="number", help="Number of resuls per page.")
    opt.add_argument("--start", dest="start", help="First result to retrieve.")
    opt.add_argument("--stop", dest="stop", help="Last result to retrieve.")
    opt.add_argument("--pause", dest="pause",
                     help="Lapse between HTTP requests, a lapse to short may cause google block your IP.")
    opt.add_argument("-c", "--country", dest="country",
                     help="Country to focus search on, similar to changing the TLD.")
    opt.add_argument("-u", "--user_agent", dest="agent", help="User agent for the HTTP requests.")

    opt.add_argument("--date", action="store_true", help=" Sort search by date.")
    opt.add_argument("--relevance", action="store_true", help=" Sort search by relevance.")

    options = opt.parse_args()

    if options.tld:
        print("[+]\tUse -d and put the tag. Eg: ./search.py -s query -d br")
        sleep(0.5)
        try:
            for tag, data in tld.items():
                print("Tag..: ", tag, " Domain..: ", data)
                sleep(0.1)
        except KeyboardInterrupt:
            pass
        exit()

    if options.tbs:
        print("[+]\t Use -t just like the examples below, e.g.: ./search.py -s query -t d10 or ./search.py -s query "
              "-min 05/05/2010 -max 10/10/2015\n")
        print("[+]\t\t***NOTE***\n -- N can be any number you want, e.g. h10, h20 and so on for any number\n")
        print("[+]  Any time(default): a")
        print("[+]  Last second or how many you want: sn")
        print("[+]  Last minute or how many you want: n")
        print("[+]  Last hour or how many you want: hn")
        print("[+]  Last days or how many you want: dn")
        print("[+]  Last weeks or how many you want: wn")
        print("[+]  Last months or how many you want: mn")
        print("[+]  Last years or how many you want: yn\n")
        print("[+]  Specific time range, E.g: From march 2 1984 to june 5 1987: -min 03/02/1987 -max 06/05/1987\n")
        exit()

    if options.search is None or options.search == "":
        opt.error("\n[-]\tPlease, insert a query to search on google. Use --help for more\n")
        exit()

    if options.domain:
        try:
            if tld[options.domain] is not None:
                options.domain = tld[options.domain]
        except KeyError:
            print("[-]\tYour TLD is incorrect, use --tld to see the available options")
            exit()

    return options


def valid_args(opt):

    if not opt.domain:
        opt.domain = "com"
    if not opt.lang:
        opt.lang = "en"

    if not opt.min or not opt.max:
        if not opt.time:
            opt.time = "qdr:a"
        else:
            opt.time = "qdr:" + opt.time
    elif re.match(r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)', opt.min) and re.match(r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)', opt.max):
        opt.time = "cdr:1,cd_min:" + str(opt.min) + ",cd_max:" + str(opt.max)
    else:
        print("\n[-]\tYour data is incorrect, verify your input. Need to be something like 03/05/2000 or 15/10/1980")
        print("[*]\tNote -- Need to be between 1901 to 2099\n")

    if not opt.number:
        opt.number = 50
    else:
        opt.number = int(opt.number)
    if not opt.start:
        opt.start = 0
    else:
        opt.start = int(opt.start)
    if not opt.stop:
        opt.stop = 25
    else:
        opt.stop = int(opt.stop)
    if not opt.pause:
        opt.pause = 3.0
    else:
        opt.pause = float(opt.pause)
    if not opt.country:
        opt.country = ""
    if not opt.agent:
        opt.agent = USER_AGENT
    if not opt.date:
        opt.date = ",sdb:1"
    else:
        opt.date = ""
    if not opt.relevance:
        opt.date = ",sdb:0"
    else:
        opt.relevance = ""

    return opt


def google_search(options):
    try:
        for url in search(options.search, tld=options.domain, lang=options.lang,
                          tbs=str(options.time) + str(options.date) + str(options.relevance), safe='off',
                          num=options.number, start=options.start, stop=options.stop, domains=None, pause=2.0,
                          country=options.country, user_agent=options.agent):
            filter_data(url)
    except KeyboardInterrupt:
        pass


def google_safe_search(options):
    try:
        for url in search(options.search, tld=options.domain, lang=options.lang,
                          tbs=options.time + options.date + options.relevance, safe='on',
                          num=options.number, start=options.start, stop=options.stop, domains=None, pause=2.0,
                          country=options.country, user_agent=options.agent):
            filter_data(url)
    except KeyboardInterrupt:
        pass


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

tld_domain_map = {
    'ac': 'ac', 'ad': 'ad', 'ae': 'ae',
    'af': 'com.af', 'ag': 'com.ag', 'ai': 'com.ai',
    'al': 'al', 'am': 'am', 'ao': 'co.ao',
    'ar': 'com.ar', 'as': 'as', 'at': 'at',
    'au': 'com.au', 'az': 'az', 'ba': 'ba',
    'bd': 'com.bd', 'be': 'be', 'bf': 'bf',
    'bg': 'bg', 'bh': 'com.bh', 'bi': 'bi',
    'bj': 'bj', 'bn': 'com.bn', 'bo': 'com.bo',
    'br': 'com.br', 'bs': 'bs', 'bt': 'bt',
    'bw': 'co.bw', 'by': 'by', 'bz': 'com.bz',
    'ca': 'ca', 'cat': 'cat', 'cc': 'cc',
    'cd': 'cd', 'cf': 'cf', 'cg': 'cg',
    'ch': 'ch', 'ci': 'ci', 'ck': 'co.ck',
    'cl': 'cl', 'cm': 'cm', 'cn': 'cn',
    'co': 'com.co', 'cr': 'co.cr', 'cu': 'com.cu',
    'cv': 'cv', 'cy': 'com.cy', 'cz': 'cz',
    'de': 'de', 'dj': 'dj', 'dk': 'dk',
    'dm': 'dm', 'do': 'com.do', 'dz': 'dz',
    'ec': 'com.ec', 'ee': 'ee', 'eg': 'com.eg',
    'es': 'es', 'et': 'com.et', 'fi': 'fi',
    'fj': 'com.fj', 'fm': 'fm', 'fr': 'fr',
    'ga': 'ga', 'ge': 'ge', 'gf': 'gf',
    'gg': 'gg', 'gh': 'com.gh', 'gi': 'com.gi',
    'gl': 'gl', 'gm': 'gm', 'gp': 'gp',
    'gr': 'gr', 'gt': 'com.gt', 'gy': 'gy',
    'hk': 'com.hk', 'hn': 'hn', 'hr': 'hr',
    'ht': 'ht', 'hu': 'hu', 'id': 'co.id',
    'ie': 'ie', 'il': 'co.il', 'im': 'im',
    'in': 'co.in', 'io': 'io', 'iq': 'iq',
    'is': 'is', 'it': 'it', 'je': 'je',
    'jm': 'com.jm', 'jo': 'jo', 'jp': 'co.jp',
    'ke': 'co.ke', 'kg': 'kg', 'kh': 'com.kh',
    'ki': 'ki', 'kr': 'co.kr', 'kw': 'com.kw',
    'kz': 'kz', 'la': 'la', 'lb': 'com.lb',
    'lc': 'com.lc', 'li': 'li', 'lk': 'lk',
    'ls': 'co.ls', 'lt': 'lt', 'lu': 'lu',
    'lv': 'lv', 'ly': 'com.ly', 'ma': 'co.ma',
    'md': 'md', 'me': 'me', 'mg': 'mg',
    'mk': 'mk', 'ml': 'ml', 'mm': 'com.mm',
    'mn': 'mn', 'ms': 'ms', 'mt': 'com.mt',
    'mu': 'mu', 'mv': 'mv', 'mw': 'mw',
    'mx': 'com.mx', 'my': 'com.my', 'mz': 'co.mz',
    'na': 'com.na', 'ne': 'ne', 'nf': 'com.nf',
    'ng': 'com.ng', 'ni': 'com.ni', 'nl': 'nl',
    'no': 'no', 'np': 'com.np', 'nr': 'nr',
    'nu': 'nu', 'nz': 'co.nz', 'om': 'com.om',
    'pa': 'com.pa', 'pe': 'com.pe', 'pg': 'com.pg',
    'ph': 'com.ph', 'pk': 'com.pk', 'pl': 'pl',
    'pn': 'co.pn', 'pr': 'com.pr', 'ps': 'ps',
    'pt': 'pt', 'py': 'com.py', 'qa': 'com.qa',
    'ro': 'ro', 'rs': 'rs', 'ru': 'ru',
    'rw': 'rw', 'sa': 'com.sa', 'sb': 'com.sb',
    'sc': 'sc', 'se': 'se', 'sg': 'com.sg',
    'sh': 'sh', 'si': 'si', 'sk': 'sk',
    'sl': 'com.sl', 'sm': 'sm', 'sn': 'sn',
    'so': 'so', 'sr': 'sr', 'st': 'st',
    'sv': 'com.sv', 'td': 'td', 'tg': 'tg',
    'th': 'co.th', 'tj': 'com.tj', 'tk': 'tk',
    'tl': 'tl', 'tm': 'tm', 'tn': 'tn',
    'to': 'to', 'tr': 'com.tr', 'tt': 'tt',
    'tw': 'com.tw', 'tz': 'co.tz', 'ua': 'com.ua',
    'ug': 'co.ug', 'uk': 'co.uk', 'uy': 'com.uy',
    'uz': 'co.uz', 'vc': 'com.vc', 've': 'co.ve',
    'vg': 'vg', 'vi': 'co.vi', 'vn': 'com.vn',
    'vu': 'vu', 'ws': 'ws', 'za': 'co.za',
    'zm': 'co.zm', 'zw': 'co.zw',
}

opt = get_arguments(tld_domain_map)

opt = valid_args(opt)

if opt.safe:
    google_safe_search(opt)
else:
    google_search(opt)
