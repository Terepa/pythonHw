import json

import requests

response = requests.get("https://api.openbrewerydb.org/breweries")
data = response.json()

for x in data:
    print(x['name'], x['brewery_type'])

with open("brewery.json", mode = "w") as write_file:
    json.dump(data, write_file, indent=4)