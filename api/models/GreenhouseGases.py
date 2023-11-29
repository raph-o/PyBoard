from __future__ import annotations

import json


class GreenhouseGases:
    def __init__(self, countryiso3code: str, date: str, value: float):
        self.countryiso3code = countryiso3code
        self.date = date
        self.value = value

    def __str__(self) -> str:
        return f'Country3isocode: {self.countryiso3code}, Date: {self.date}, Value: {self.value}'

    @classmethod
    def from_json(cls, json_data: dict) -> list[GreenhouseGases]:
        """
        Créer une liste de résultats à partir d'un dictionnaire

        Args:
            json_data: Dictionnaire décrivant une liste de résultats

        Returns:
            Liste d'objets Results contenant les valeurs du dictionnaire, et exlucant les résultats sans valeur
        """
        results = []
        for item in json_data:
            countryiso3code = item.get('countryiso3code')
            date = item.get('date')
            value = item.get('value')

            if value is None:
                continue

            result = cls(countryiso3code, date, value)
            results.append(result)
        return results

    @classmethod
    def extract_results(cls, json_dict: dict) -> list[GreenhouseGases]:
        """
        Extrait les informations d'un dictionnaire json

        Args:
            json_dict: Dictionnaire représentant une liste d'objets Results
        Returns:
            Liste d'objet Results
        """
        return GreenhouseGases.from_json(json_dict[1])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Results'

        Returns:
            Objet Results sous forme de chaîne json
        """
        result_dict = {
            'countryiso3code': self.countryiso3code,
            'date': self.date,
            'value': self.value
        }

        return json.dumps(result_dict)
