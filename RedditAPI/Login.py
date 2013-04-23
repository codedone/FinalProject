
from pprint import pprint
import requests
import json

username = 'CodedOne'
password = 'squidharder9976'

user_pass_dict = {'user': username,
    'passwd': password,
    'api_type': 'json',}

headers = {'user-agent': 'this is a test bot',}

client = requests.session()
client.headers = headers

r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)

j = json.loads(r.content)

client.modhash = j['json']['data']['modhash']

print '{USER}\'s modhash is: {mh}'.format(USER=username, mh=client.modhash)
