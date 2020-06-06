import re
import save_results
from date import extract_date


def filter_two_dots(url, content, csv):
    lista = []
    date = extract_date(content)
    lista.append(str(date) + ";" + url + ";\n\n")

    content = content.split("<textarea id=\"paste_code\" class=\"paste_code\" name=\"paste_code\" onkeydown=\"return catchTab(this,event)\">")[1]
    content = content.split("</textarea>")[0]

    for item in re.split('\W\w\W\w', content):
        for item2 in re.split('\s', item):
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?:.*', item2):
                email = item2.split(":")[0]
                senha = item2.split(":")[1]
                if re.search(r'\|', senha):
                    senha = senha.split('|')[0]
                elif re.search(r';', senha):
                    senha = senha.split(';')[0]
                elif re.search(r':', senha):
                    senha = senha.split(':')[0]

                if csv:
                    lista.append(str(email) + ";" + str(senha) + ";\n")
                else:
                    lista.append(str(email) + "+" + str(senha) + "\n")

    if csv:
        file_name = url.split("/")[-1]
        file_name = "csv/leakbuster_" + file_name.split(".")[0]
        save_results.saveContentCSV(file_name, lista)
    else:
        file_name = url.split("/")[-1]
        file_name = "downloads/leakbuster_" + file_name.split(".")[0]
        save_results.saveContent(file_name, lista)


def filter_module(url, content, csv):
    lista = []
    date = extract_date(content)
    lista.append(str(date) + ";" + url + ";\n\n")

    content = content.split("<textarea id=\"paste_code\" class=\"paste_code\" name=\"paste_code\" onkeydown=\"return catchTab(this,event)\">")[1]
    content = content.split("</textarea>")[0]

    for item in re.split('\W\w\W\w', content):
        for item2 in re.split('\s', item):
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?\|.*', item2):
                email = item2.split("|")[0]
                senha = item2.split("|")[1]
                if re.search(r'\|', senha):
                    senha = senha.split('|')[0]
                elif re.search(r';', senha):
                    senha = senha.split(';')[0]
                elif re.search(r':', senha):
                    senha = senha.split(':')[0]

                if csv:
                    lista.append(str(email) + ";" + str(senha) + ";\n")
                else:
                    lista.append(str(email) + "+" + str(senha) + "\n")

    if csv:
        file_name = url.split("/")[-1]
        file_name = "csv/leakbuster_" + file_name.split(".")[0]
        save_results.saveContentCSV(file_name, lista)
    else:
        file_name = url.split("/")[-1]
        file_name = "downloads/leakbuster_" + file_name.split(".")[0]
        save_results.saveContent(file_name, lista)


def filter_dot_comma(url, content, csv):
    lista = []
    date = extract_date(content)
    lista.append(str(date) + ";" + url + ";\n\n")

    content = content.split("<textarea id=\"paste_code\" class=\"paste_code\" name=\"paste_code\" onkeydown=\"return catchTab(this,event)\">")[1]
    content = content.split("</textarea>")[0]

    for item in re.split('\W\w\W\w', content):
        for item2 in re.split('\s', item):
            if re.search(r'[a-z0-9._%+]+@[a-z0-9.-]+\.[a-z]{2,}[ ]?;.*', item2):
                email = item2.split(";")[0]
                senha = item2.split(";")[1]
                if re.search(r'\|', senha):
                    senha = senha.split('|')[0]
                elif re.search(r';', senha):
                    senha = senha.split(';')[0]
                elif re.search(r':', senha):
                    senha = senha.split(':')[0]

                if csv:
                    lista.append(str(email) + ";" + str(senha) + ";\n")
                else:
                    lista.append(str(email) + "+" + str(senha) + "\n")

    if csv:
        file_name = url.split("/")[-1]
        file_name = "csv/leakbuster_" + file_name.split(".")[0]
        save_results.saveContentCSV(file_name, lista)
    else:
        file_name = url.split("/")[-1]
        file_name = "downloads/leakbuster_" + file_name.split(".")[0]
        save_results.saveContent(file_name, lista)


def download_raw_content(url, content, csv):
    lista = []
    date = extract_date(content)
    lista.append(str(date) + ";" + url + ";\n\n")

    content = content.split("<textarea id=\"paste_code\" class=\"paste_code\" name=\"paste_code\" onkeydown=\"return catchTab(this,event)\">")[1]
    content = content.split("</textarea>")[0]

    for item in re.split('\W\w\W\w', content):

        if csv:
            lista.append(str(item) + ";\n")
        else:
            lista.append(str(item) + "\n")

    if csv:
        file_name = url.split("/")[-1]
        file_name = "csv/leakbuster_" + file_name.split(".")[0]
        save_results.saveContentCSV(file_name, lista)
    else:
        file_name = url.split("/")[-1]
        file_name = "downloads/leakbuster_" + file_name.split(".")[0]
        save_results.saveContent(file_name, lista)
