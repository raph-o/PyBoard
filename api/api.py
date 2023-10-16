
import requests

from api.Results import Results


def get_data() -> list[Results]:
    url = 'https://api.worldbank.org/V2/fr/country/all/indicator/EN.ATM.GHGT.KT.CE?format=json&per_page=16758'

    response = requests.get(url)
    jsonResponse = response.json()

    """informations = Informations.extract_informations(jsonResponse)
    print(informations)"""

    return Results.extract_results(jsonResponse)
