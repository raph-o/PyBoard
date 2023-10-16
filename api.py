from Informations import Informations
from Results import Results

import requests

url = 'https://api.worldbank.org/V2/fr/country/all/indicator/EN.ATM.GHGT.KT.CE?format=json&per_page=1000'

response = requests.get(url)
jsonResponse = response.json()

informations = Informations.extract_informations(jsonResponse)
print(informations)

results = Results.extract_results(jsonResponse)
for result in results:
    print(result)
