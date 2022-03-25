from app.leakbuster import app
from Crypto.Cipher import AES
import base64
import unidecode


def encrypt(data):
    key = app.config['SECRET_KEY']
    symmetric = False
    clean_text = unidecode.unidecode(data)
    cont = len(clean_text)
    while not symmetric:
        if (cont % 16) == 0:
            symmetric = True
        else:
            cont += 1

    aes = AES.new(key.encode(), AES.MODE_ECB)
    crypted_text = aes.encrypt(clean_text.rjust(cont).encode())
    crypted_text = base64.b64encode(crypted_text)
    return crypted_text.decode()


def decrypt(data):
    try:
        key = app.config['SECRET_KEY']
        aes = AES.new(key.encode(), AES.MODE_ECB)
        crypted_text = data.encode()
        crypted_text = base64.b64decode(crypted_text)
        clean_text = aes.decrypt(crypted_text)
        clean_text = clean_text.decode('utf-8')
        return clean_text.lstrip()
    except Exception:
        return data
