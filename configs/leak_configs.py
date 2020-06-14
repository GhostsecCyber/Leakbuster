from termcolor import cprint, colored
from menu import default_menu
import subprocess as command


def clear_configs():
    command.call(['clear'])
    default_menu()


def leak_config_options():

    cprint("Select from the menu:\n", 'red')
    cprint("\t1) Register New emails and passwords.", 'red')
    cprint("\t2) View all emails and passwords registered.", 'red')
    cprint("\t3) Show basic configs.", 'red')
    cprint("\t4) Help.\n", 'red')
    cprint("\t99) Return to main menu.\n\n", 'red')

    resp = int(input(colored("LBT> ", 'cyan')))

    if resp == 99:
        resp = 0
        from leakbuster import LeakBuster
        LeakBuster()
    elif resp == 1:
        clear_configs()
        print("Under Development\n")
        input(colored("LBT> ", 'cyan'))
    elif resp == 2:
        clear_configs()
        print("Under Development\n")
        input(colored("LBT> ", 'cyan'))
    elif resp == 3:
        clear_configs()
        print("Under Development\n")
        input(colored("LBT> ", 'cyan'))
    elif resp == 4:
        clear_configs()
        print("Under Development\n")
        input(colored("LBT> ", 'cyan'))
    else:
        clear_configs()
        leak_config_options()


