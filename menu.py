from termcolor import cprint, colored
import subprocess as command
import random


def default_menu():
    command.call(['clear'])
    print_title()
    intro()
    description()


def print_title():
    number = random.randrange(6)

    if number == 0:
        print(colored("\t\t  _               _    ____            _", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t | |    ___  __ _| | _| __ ) _   _ ___| |_ ___ _ __", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t | |   / _ \/ _` | |/ /  _ \| | | / __| __/ - \ '__|", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t | |__|  __/ (_| |   <| |_) | |_| \__ \ ||  __/ |", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t |_____\___|\__,_|_|\_\____/ \__,_|___/\__\___|_|", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                         Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    elif number == 1:
        print(colored("\t\t ____ _____ _____ ____            _ ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t|  _ \___ /|  ___| __ ) _   _ ___| |_ ___ _ __ ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t| | | ||_ \| |_  |  _ \| | | / __| __/ _ \ '__| ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t| |_| |__) |  _| | |_) | |_| \__ \ ||  __/ | ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t|____/____/|_|   |____/ \__,_|___/\__\___|_| ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                  Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    elif number == 2:
        print(colored("\t\t    ____ _____ ________________  _   _______", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t   / __ \__  // ____/ ____/ __ \/ | / / ___/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t  / / / //_ </ /_  / /   / / / /  |/ / __ \ ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t / /_/ /__/ / __/ / /___/ /_/ / /|  / /_/ /", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t/_____/____/_/    \____/\____/_/ |_/\____/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                  Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    elif number == 3:
        print(colored("\t\t    __               __   ______            _____", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t   / /   ___  ____ _/ /__/ ____/___  ____  / ___/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t  / /   / _ \/ __ `/ //_/ /   / __ \/ __ \/ __ \ ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t / /___/  __/ /_/ / ,< / /___/ /_/ / / / / /_/ /", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t/_____/\___/\__,_/_/|_|\____/\____/_/ /_/\____/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                      Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    elif number == 4:
        print(colored("\t\t    ____ _____ __________             __", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t   / __ \__  // ____/ __ )__  _______/ /____  _____", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t  / / / //_ </ /_  / __  / / / / ___/ __/ _ \/ ___/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t / /_/ /__/ / __/ / /_/ / /_/ (__  ) /_/  __/ /", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t/_____/____/_/   /_____/\__,_/____/\__/\___/_/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                     Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    elif number == 5:
        print(colored("\t\t _               _     ____             __   ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t| |    ___  __ _| | __/ ___|___  _ __  / /_  ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t| |   / _ \/ _` | |/ / |   / _ \| '_ \| '_ \ ", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t| |__|  __/ (_| |   <| |__| (_) | | | | (_) |", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t|_____\___|\__,_|_|\_\____|\___/|_| |_|\___/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                   Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))
    else:
        print(colored("\t\t    __               __   ____             __", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t   / /   ___  ____ _/ /__/ __ )__  _______/ /____  _____", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t  / /   / _ \/ __ `/ //_/ __  / / / / ___/ __/ _ \/ ___/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t / /___/  __/ /_/ / ,< / /_/ / /_/ (__  ) /_/  __/ /", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t/_____/\___/\__,_/_/|_/_____/\__,_/____/\__/\___/_/", 'red', attrs=['dark', 'bold']))
        print(colored("\t\t                          Developed by: D3FCON6\n", 'green', attrs=['dark', 'bold', 'blink']))


def intro():
    print(colored("[---]\t\t", 'blue', attrs=['bold']), colored("LeakBuster (LBT)", 'yellow', attrs=['bold']), colored(" - Web crawler and leak monitoring\t[---]", 'blue', attrs=['bold']))
    print(colored("[---]\t\tCreated by: ", 'blue', attrs=['bold']), colored("th3r4ven, SC00T3RB0Y", 'yellow', attrs=['bold']), colored("\t\t\t[---]", 'blue', attrs=['bold']))
    print(colored("[---]\t\tProjected by: ", 'blue', attrs=['bold']), colored("S1dBoy, RSAKing, Jucamilly", 'yellow', attrs=['bold']), colored("\t\t[---]", 'blue', attrs=['bold']))
    print(colored("[---]\t\tDesign by: ", 'blue', attrs=['bold']), colored("th3r4ven, SC00T3RB0Y, GaloAgiota", 'yellow', attrs=['bold']), colored("\t\t[---]", 'blue', attrs=['bold']))
    print(colored("\t\t\t\tVersion: ", 'blue', attrs=['bold']), colored("2.2", 'red', attrs=['bold']))


def description():
    print(colored("\t\tWelcome to LeakBuster framework", 'green', attrs=['bold']))
    print(colored("\tAn active Web crawler monitoring for email and password leak\n", 'green', attrs=['bold']))
    print(colored("\t\tLeakBuster is a product of D3FCON6.\n\n", 'green', attrs=['bold']))


def main_options():
    cprint("Select from menu:\n", 'red')
    cprint("\t1) Configuration.", 'red')
    cprint("\t2) Google search.", 'red')
    cprint("\t3) Confirm login found on pages.", 'red')
    cprint("\t4) Update LeakBuster.", 'red')
    cprint("\t5) Help, Credits and about.\n", 'red')
    cprint("\t99) Exit LeakBuster Framework.\n\n", 'red')

    resp = int(input(colored("LBT> ", 'cyan')))
    return resp
