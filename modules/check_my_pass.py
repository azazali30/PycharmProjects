import requests
import hashlib


def request_api_data(query_char):
    res = requests.get('https://api.pwnedpasswords.com/range/aaf4c')
    if res.status_code == 200:
        return res.text
    return "Not found"


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(sha1password)
    # print(sha1password[0:5])
    first5_chars, tail = sha1password[:5], sha1password[5:]
    data = request_api_data(first5_chars)
    dictionary = {}
    for line in data.splitlines(False):
        key_val = line.split(':')
        dictionary[key_val[0]] = key_val[1]
        if key_val[0] == sha1password:
            print(f'new Pass: {line} =========== {key_val[0]} =========== {key_val[1]}')
    print(f"{sha1password}", dictionary[tail])


pwned_api_check("hello")
