import requests
import json

pn = int(input())
data = requests.get(
    "https://jsonmock.hackerrank.com/api/article_users?page="+str(pn)).text

names = []
response = json.loads(data)

main_data = response['data']
for dic in main_data:
    if dic['submission_count'] > 2000:
        names.append(dic['username'])

print(names)
