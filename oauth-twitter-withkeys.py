from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
# print (r.text)

python_obj = json.loads(r.text)
# print(python_obj.keys()) #(['statuses', 'search_metadata'])
# print(type(python_obj["statuses"])) #list
# print(type(python_obj["statuses"][0])) #dict
# print(python_obj["statuses"][0].keys()) #text is a key!
# print(python_obj["statuses"][0]["text"])

for item in python_obj["statuses"]:
    print(item['user']['name'])
    print(item["text"])
    print("\n")
