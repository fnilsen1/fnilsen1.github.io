import requests, random

url = f"https://countriesnow.space/api/v0.1/countries/capital"
resultat = requests.get(url)
data = resultat.json()

pp = input('What is your country: ')
ratata = 0
for country in data['data']:
    if country['name'] == pp:
        print('the capital is ' + country['capital'])
        ratata += 1

if ratata == 0:
    print('That country does not exist.')