from __future__ import annotations

import json

"""
Classe permettant l'instanciation d'un objet représentant les taux d'émmission de gaz à effet de serre pour un pays donné par son iso2code.
Voici un exemple d'objet json utilisé pour l'instanciation provenant d'un appel fait vers l'api :
{
  "indicator": {
    "id": "EN.ATM.GHGT.KT.CE",
    "value": "Émissions totales de GES (kt d’équivalent CO2)"
  },
  "country": {
    "id": "FR",
    "value": "France"
  },
  "countryiso3code": "FRA",
  "date": "2014",
  "value": 427859.1918,
  "unit": "",
  "obs_status": "",
  "decimal": 0
}

Ici, nous ne prenons que l'iso2code, étant l'id du pays, le taux d'émission de gaz à effet de serre pour une date données.
Une requête pour récupérer ces informations :
    GET https://api.worldbank.org/V2/fr/country/all/indicator/EN.ATM.GHGT.KT.CE?format=json&most_recent_year_desc=false&per_page=16758
"""
class GreenhouseGases:
    def __init__(self, countryiso2code: str, date: str, value: float):
        self.countryiso2code = countryiso2code
        self.date = date
        self.value = value

    def __str__(self) -> str:
        return f'Country3isocode: {self.countryiso2code}, Date: {self.date}, Value: {self.value}'

    @classmethod
    def from_json(cls, json_data: dict) -> list[GreenhouseGases]:
        """
        Créer une liste de résultats à partir d'un dictionnaire

        :param: json_data: Dictionnaire décrivant une liste de résultats
        :return: Liste d'objets Results contenant les valeurs du dictionnaire, et exlucant les résultats sans valeur
        """
        results = []
        for item in json_data:
            countryiso2code = item.get('country')["id"]
            date = item.get('date')
            value = item.get('value')

            if value is None:
                continue

            result = cls(countryiso2code, date, value)
            results.append(result)
        return results

    @classmethod
    def extract_results(cls, json_dict: dict) -> list[GreenhouseGases]:
        """
        Extrait les informations d'un dictionnaire json

        :param: json_dict: Dictionnaire représentant une liste d'objets Results
        :return: Liste d'objet Results
        """
        return GreenhouseGases.from_json(json_dict[1])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Results'

        :return: Objet Results sous forme de chaîne json
        """
        result_dict = {
            'countryiso2code': self.countryiso2code,
            'date': self.date,
            'value': self.value
        }

        return json.dumps(result_dict)
