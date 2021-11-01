import requests

response = requests.get("https://api.openbrewerydb.org/breweries")
data = response.json()

for x in data:
    print(x['name'], x['brewery_type'])