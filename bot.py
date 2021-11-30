import requests
import os
import sys
import random
import string
import json

url = 'https://www.underskrift.no/signer.asp'

first_names = json.loads(open('names/first.json').read())
last_names = json.loads(open('names/last.json').read())

while True:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = first_name + ' ' + last_name

    email = first_name + last_name + ''.join(random.choice(string.digits) for i in range(5)) + '@gmail.com'

    payload = {'VisEpost': 0, 'Kampanje': 9810, 'Navn': username, 'Epost': email}
    try: 
        r = requests.post(url, allow_redirects=False, data=payload)
        print(r.status_code, 'Sending name %s and email %s' % (username, email))

    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred:" + repr(errh))

    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred:" + repr(errt))

    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred" + repr(err))

