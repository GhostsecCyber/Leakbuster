def saveContentCSV(file_name, lista):

    with open(file_name + ".csv", "wt") as out_file:
        for data in lista:
            out_file.write(data)
    out_file.close()


def save_raw_content(file_name, content):

    with open(file_name + ".csv", "wt") as out_file:
        out_file.write(content)
    out_file.close()

