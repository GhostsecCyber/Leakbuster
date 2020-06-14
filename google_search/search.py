
from google_search.filter import filter_data
from termcolor import cprint

try:
    from googlesearch import search
except ImportError:
    print(
        "No module named 'google' found. Try run the following commands: pip install beautifulsoup4 and pip install google")
    exit()


def google_search(query, domains):
    # Function responsible for searching in google and return the URL,
    # then send to other function to filter the results.

    cprint("\n[+]  Your search is in progress, enjoy the view while LeakBuster grab everything for you...", 'red')

    try:
        for url in search(query, tld='com', lang='en',
                          tbs='qdr:a', safe='off',
                          num=200, start=0, stop=50, domains=domains, pause=2.0,
                          country='', user_agent=None):
            filter_data(url)
        cprint("[+]  The search has been completed, you can find the extracted data on results/csv directory\n", 'red')
    except KeyboardInterrupt:
        cprint("[-]  Search interrupted, you can find the extracted data on results/csv directory\n", 'red')


def default_google_search(query):  # Main function
    domain = ["pastebin.com"]

    google_search(query, domain)
