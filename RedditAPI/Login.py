
# used tankorsmash's tutorial:
# http://blog.tankorsmash.com/?p=295

from pprint import pprint
import requests
import json

def login(username, password):

    user_pass_dict = {'user': username,
        'passwd': password,
        'api_type': 'json',}

    headers = {'user-agent': 'CSCE315 FinalProject',}

    client = requests.session()
    client.headers = headers

    r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)

    j = json.loads(r.content)

    client.modhash = j['json']['data']['modhash']
    client.user = username

    return client
