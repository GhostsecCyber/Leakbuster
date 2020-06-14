#!/usr/bin/env python

import re
from termcolor import cprint, colored
from menu import default_menu
from texttable import Texttable
import pickle


def configuration_menu():
    default_menu()
    cprint("Select from menu:\n", 'red')
    cprint("\t1) Viw/Edit configuration.", 'red')
    cprint("\t2) Reset configuration.\n", 'red')
    cprint("\t99) Return to previous menu:\n\n", 'red')

    resp = int(input(colored("LBT> ", 'cyan')))

    if resp == 99:
        from google_search.search_options import leak_search_options_menu
        leak_search_options_menu()
    elif resp == 1:
        handle_keys()
    elif resp == 2:
        default_menu()
        reset_keys_param()
        cprint("\n\nYour configs has been redefined, press any key to continue", 'red')
        input(colored("LBT> ", 'cyan'))
        configuration_menu()
    else:
        configuration_menu()


def handle_keys():
    default_menu()
    key = get_keys_values()
    t = Texttable()
    for x in key.keys():
        t.add_rows([['key', 'value', 'type', 'info'], [str(x), str(key[x][0]), str(key[x][1]), str(key[x][2])]])
    cprint(t.draw(), 'red')

    cprint("\n To change the target domains, just type domain and you will be prompted to put\n  as many domains as "
           "you want, for other configs, just type the key followed by = and the value", 'red')

    cprint("\n Want to change configurations?(y/n)", 'red')
    resp = input(colored("LBT> ", 'cyan')).lower()

    if resp == 'y':
        validate_key_value()
    else:
        configuration_menu()


def validate_key_value():
    param = get_keys_values()

    cprint("Enter your key and value next like: top=com.br or domain to configure target domains", 'red')
    resp = input(colored("LBT> ", 'cyan')).lower()

    if re.search('=', resp):
        key = resp.split("=")[0]
        value = resp.split("=")[1]

        if key in param.keys():
            if key == 'top':
                param[key] = [value, 'string', 'Top google domain level.']

            elif key == 'lang':
                param[key] = [value, 'string', 'Google search language.']

            elif key == 'time':
                value = "qdr:" + value
                param[key] = [value, 'string', 'Filter search by the last sec(sn), min(n), hours(hn), days(dn), '
                                               'months(mn) and years(yn), letter a is anytime, n can be any number '
                                               'you want.']

            elif key == 'min':
                if re.match(r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|(('
                            r'29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])('
                            r'00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)', value):
                    param[key] = ["cdr:1,cd_min:" + str(value), 'string', 'Starts the search on the minimum date.']
                else:
                    param[key] = ["", 'string', 'Starts the search on the minimum date.']

            elif key == 'max':
                if re.match(r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|(('
                            r'29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])('
                            r'00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)', value):
                    param[key] = [",cd_max:" + str(value), 'string', 'Ends the search on the maximum date.']
                else:
                    param[key] = ["", 'string', 'Ends the search on the maximum date.']

            elif key == 'safe':
                if value.lower() == 'true':
                    param[key] = [True, 'boolean', 'Activate a safe search on google']
                else:
                    param[key] = [False, 'boolean', 'Activate a safe search on google']
            elif key == 'start':
                param[key] = [int(value), 'int', 'First result to retrieve.']

            elif key == 'stop':
                param[key] = [int(value), 'int', 'Last result to retrieve (put None to keep searching forever).']

            elif key == 'pause':
                param[key] = [value, 'float', 'Lapse between HTTP requests (Don\'t put less than 2.0).']

            elif key == 'user_agent':
                param[key] = [value, 'string', 'User Agent to be send in the request']

            elif key == 'date':
                if value.lower() == 'true':
                    param[key] = [True, 'boolean', 'Sort search by date']
                else:
                    param[key] = [False, 'boolean', 'Sort search by date']

            else:
                if value.lower() == 'true':
                    param[key] = [True, 'boolean', 'Sort search by relevance' + '\n\n']
                else:
                    param[key] = [False, 'boolean', 'Sort search by relevance' + '\n\n']

            if param['min'][0] != '' and param['max'][0] != '':
                param['time'] = [str(param['min'][0] + param['max'][0]), 'string',
                                 'Filter search at a specific time range.']

            save_keys_values(param)
            handle_keys()

        else:
            print("Your key is incorrect.\n")
            validate_key_value()

    elif resp == 'domain':
        domains = []
        resp = "y"
        while resp == "y":
            cprint("\nInsert a domain to focus your search:", 'red')
            domains.append(input(colored("LBT> ", 'cyan')).lower())
            resp = input(colored("\n Want to search in others domains too? (y/n)", 'red')).lower()

        param['domain'] = [domains, 'array', 'Target sites to focus search.']
        save_keys_values(param)
        handle_keys()
    else:
        validate_key_value()


def get_keys_values():
    with open('custom_google_search/custom_search_param.txt', 'rb') as arq:
        keys = pickle.load(arq)
    arq.close()

    return keys


def save_keys_values(keys):
    with open('custom_google_search/custom_search_param.txt', 'wb') as arq:
        pickle.dump(keys, arq)
    arq.close()


def reset_keys_param():
    domains = ["pastebin.com"]
    keys = {
        "top": ['com', 'string', 'Top google domain level.'],
        "domain": [domains, 'array', 'Target sites to focus search.'],
        "lang": ['en', 'string', 'Google search language.'],
        "time": ['a', 'string', 'Filter search by the last sec(sn), min(n), hours(hn), days(dn), months(mn) and '
                                'years(yn), letter a is anytime, n can be any number you want.'],
        "min": ['', 'string', 'Starts the search on the minimum date.'],
        "max": ['', 'string', 'Ends the search on the maximum date.'],
        "safe": [False, 'boolean', 'Activate a safe search on google'],
        "start": [0, 'int', 'First result to retrieve.'],
        "stop": [50, 'int', 'Last result to retrieve (put None to keep searching forever).'],
        "pause": [2.0, 'float', 'Lapse between HTTP requests.'],
        "user_agent": ['', 'string', 'User Agent to be send in the request'],
        "date": [False, 'boolean', 'Sort search by date'],
        "relevance": [False, 'boolean', 'Sort search by relevance']
    }

    save_keys_values(keys)

