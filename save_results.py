
def saveEmailPassword(file_name, lista):

    with open(file_name + ".txt", "wt") as out_file:
        for data in lista:
            out_file.write(data)
        print("[+]\t\t Downloaded, filtered and saved successfully on: " + file_name)
    out_file.close()


def saveContent(file_name, lista):

    with open(file_name + ".txt", "wt") as out_file:
        for data in lista:
            out_file.write(data)
        print("[+]\t\t Downloaded, filtered and saved successfully on: " + file_name)
    out_file.close()


def saveContentCSV(file_name, lista):

    with open(file_name + ".csv", "wt") as out_file:
        for data in lista:
            out_file.write(data)
        print("[+]\t\t Downloaded, filtered and saved successfully on: " + file_name)
    out_file.close()


