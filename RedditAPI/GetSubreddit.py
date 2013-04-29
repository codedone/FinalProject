
# used tankorsmash's tutorial:
# blog.tankorsmash.com/?p=378

import json
import requests

def subredditInfo(client, limit=10, sr='all', 
    sorting='', return_json=False, **kwargs):

    parameters = {'limit': limit}
    parameters.update(kwargs)
    
    url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
    r = client.get(url, params=parameters)

    j = json.loads(r.text)

    if return_json:
        return j
    else:
        stories = []
        for story in j['data']['children']:
            stories.append(story)

        return stories
