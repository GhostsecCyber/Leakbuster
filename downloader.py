def downloader(url, content):

    file_name = url.split("/")[-1]
    file_name = "downloads/" + "leakbuster_" + file_name.split(".")[0]

    with open(file_name + ".html", "w") as out_file:
        out_file.write(content)
        print("[+]\tDownloaded and saved successfully on: " + file_name)
