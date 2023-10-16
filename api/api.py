from Informations import Informations
from Results import Results

import requests


def get_data() -> list[Results]:
    url = 'https://api.worldbank.org/V2/fr/country/all/indicator/EN.ATM.GHGT.KT.CE?format=json&per_page=1000'

    response = requests.get(url)
    jsonResponse = response.json()

    """informations = Informations.extract_informations(jsonResponse)
    print(informations)"""

    return Results.extract_results(jsonResponse)
