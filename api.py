from Informations import Informations

import requests

url = 'https://api.worldbank.org/V2/fr/country/all/indicator/EN.ATM.GHGT.KT.CE?format=json&per_page=10'

response = requests.get(url)
jsonResponse = response.json()

informations = Informations.extract_informations(jsonResponse)
print(informations)
