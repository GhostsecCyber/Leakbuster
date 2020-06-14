#!/usr/bin/env python

from menu import default_menu, main_options
from configs.leak_configs import leak_config_options
from google_search.search_options import leak_search_options_menu
from custom_google_search.custom_search_configs import reset_keys_param
import subprocess as command
import os.path

if not os.path.exists("results"):
    command.call(["mkdir", "results"])
    command.call(["mkdir", "results/downloads", '-p'])
    command.call(["mkdir", "results/csv", '-p'])
if not os.path.exists('custom_google_search/custom_search_param.txt'):
    command.call(['touch', 'custom_google_search/custom_search_param.txt'])
    reset_keys_param()


def reset():
    resp = 0
    default_menu()


def LeakBuster():
    try:
        reset()
        resp = main_options()

        if resp == 99:
            reset()
            print("\n\n[-] Exiting LeakBuster Framework....\n")
            exit()
        elif resp == 1:
            reset()
            leak_config_options()
        elif resp == 2:

            leak_search_options_menu()

        elif resp == 3:
            reset()
            LeakBuster()
        elif resp == 5:
            print("reade.md")
        else:
            LeakBuster()

    except KeyboardInterrupt:
        print("\n\n[-] Exiting LeakBuster Framework....\n")
        exit()
    except ValueError:
        LeakBuster()


LeakBuster()
