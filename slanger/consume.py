import facebook    #sudo pip install facebook-sdk
import itertools
import json
import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# access_token = os.getenv("FB_ACCESS_TOKEN")
access_token = '501047351025171|6ecee5e1d01303d695613d1e4a84e2a7'
print(access_token)
user = 'leehsienloong'

graph = facebook.GraphAPI(access_token)

profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

count = 0
for i in JDict['data']:
    allID = i['id']
    try:
        allComments = i['comments']

        for a in allComments['data']:  
            count += 1
            print (a['message'])


    except (UnicodeEncodeError):
        pass


print (count)