import requests
import json
from collections import defaultdict
data = requests.get(
    "https://npiregistry.cms.hhs.gov/api/?version=2.0&city=boston").text


response = json.loads(data)
main_data = response['results']
simple_data = defaultdict(list)
basic = defaultdict(list)
addresses = defaultdict(list)
taxonomies = defaultdict(list)


for dics in main_data:
    for key, values in dics.items():

        if type(values) != dict and type(values) != list:
            simple_data[key].append(values)

        elif key == 'addresses':
            for key, val in values.items():
                addresses[key].append(val)

        elif key == 'basic':
            for key, val in values.items():
                basic[key].append(val)

        elif key == 'taxonomies':
            for key, val in values.items():
                taxonomies[key].append(val)


print(simple_data, end="\n")
print(basic, end="\n")
print(addresses, end="\n")
print(taxonomies, end="\n")
