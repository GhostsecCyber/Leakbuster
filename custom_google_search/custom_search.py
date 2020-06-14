from custom_google_search.custom_search_configs import get_keys_values
from custom_google_search.filter import filter_data
from termcolor import cprint

try:
    from googlesearch import search
except ImportError:
    print(
        "No module named 'google' found. Try run the following commands: pip install beautifulsoup4 and pip install "
        "google")


def google_search(query, param):
    cprint("\n[+]  Your search is in progress, enjoy the view while LeakBuster grab everything for you...", 'red')

    try:
        for url in search(query, tld=param['top'][0], lang=param['lang'][0],
                          tbs=str(param['time'][0]) + str(param['date'][0]) + str(param['relevance'][0]), safe='off',
                          num=200, start=param['start'][0], stop=param['stop'][0], domains=param['domain'][0],
                          pause=param['pause'][0],
                          country='', user_agent=param['user_agent'][0]):
            filter_data(url)
        cprint("[+]  The search has been completed, you can find the extracted data on results/csv directory\n", 'red')
    except KeyboardInterrupt:
        cprint("[-]  Search interrupted, you can find the extracted data on results/csv directory\n", 'red')


# Function responsible for safe searching in google and return the URL,
# then send to other function to filter the results.


def google_safe_search(query, param):
    print("[+]\tSafe search in progress...\n")
    try:
        for url in search(query, tld=param['top'][0], lang=param['lang'][0],
                          tbs=str(param['time'][0]) + str(param['date'][0]) + str(param['relevance'][0]), safe='on',
                          num=200, start=param['start'][0], stop=param['stop'][0], domains=param['domain'][0],
                          pause=param['pause'][0],
                          country='', user_agent=param['user_agent'][0]):
            filter_data(url)
        print("[+]\tThe search has been completed, you can find the extracted data on results/csv directory\n")
    except KeyboardInterrupt:
        print("[-]  Search interrupted, you can find the extracted data on results/csv directory\n")


def custom_google_search(query):
    keys = get_keys_values()

    if keys['safe'] is True:
        google_safe_search(query, keys)
    else:
        google_search(query, keys)
