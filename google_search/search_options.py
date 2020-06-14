from termcolor import cprint, colored
from menu import default_menu
from google_search.search import default_google_search
from custom_google_search.custom_search_configs import configuration_menu
from custom_google_search.custom_search import custom_google_search


def info_default_search():
    cprint("Info:\n", 'red')
    cprint("\tThis option make a search on google with a query of your choice.", 'red')
    cprint("\tAnd will analyse 50 results and save all positive results in csv files.\n\n", 'red')


def leak_search_options_menu():
    default_menu()
    cprint("Select from menu:\n", 'red')
    cprint("\t1) Configure custom search parameters.", 'red')
    cprint("\t2) Custom search.", 'red')
    cprint("\t3) Default search.", 'red')
    cprint("\t4) Help.\n", 'red')
    cprint("\t99) Return to main menu.\n\n", 'red')

    resp = int(input(colored("LBT> ", 'cyan')))

    if resp == 99:

        resp = 0
        from leakbuster import LeakBuster
        LeakBuster()

    elif resp == 1:

        configuration_menu()

    elif resp == 2:

        default_menu()
        cprint("Insert what you want to search on google:\n", 'red')
        query = input(colored("LBT> ", 'cyan'))
        custom_google_search(query)
        cprint("Press any key to return to previous menu", 'red')
        input(colored("LBT>", 'cyan'))
        from leakbuster import LeakBuster
        LeakBuster()

    elif resp == 3:

        default_menu()
        info_default_search()
        cprint("Insert what you want to search on google:\n", 'red')
        query = input(colored("LBT> ", 'cyan'))
        default_google_search(query)
        cprint("Press any key to return to previous menu", 'red')
        input(colored("LBT>", 'cyan'))
        from leakbuster import LeakBuster
        LeakBuster()

    elif resp == 4:

        default_menu()
        leak_search_options_menu()

    else:
        default_menu()
        leak_search_options_menu()


