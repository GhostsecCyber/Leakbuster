def extract_date(data):
    data = data.split('<span title="')[1]

    return data.split('">')[0]