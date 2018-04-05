import facebook
import json
import requests

token = ''
# update before using

graph=facebook.GraphAPI(access_token=token)
page_info=graph.get_object('me')
page_ID=page_info['id']

def page_data(page_id,access_token):
    try:
        object=requests.get(url,params=parameters).text.encode('utf-8')

        try:
            return json.loads(object)
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except (IOError, e):
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

base='https://graph.facebook.com/v2.9'
node='/'+ page_ID + '/feed?fields=likes'
url=base+node
parameters={'period':'week','access_token':token}
data = page_data(url, parameters)

# result
print(data['data'][0]['likes']['data'][0])
