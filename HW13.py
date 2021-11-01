import requests

response = requests.get("https://api.openbrewerydb.org/breweries")
data = response.json()

for x in data:
    print(x['name'], x['brewery_type'])

    food = "kartupelis"
    d = {c: c.upper() * 2 for c in food}
    print(d['c'])