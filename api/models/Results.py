from __future__ import annotations
import json


class Results:
    def __init__(self, country: str, date: str, value: float):
        self.country = country
        self.country = country
        self.date = date
        self.value = value

    @classmethod
    def from_json(cls, json_data: dict) -> list[Results]:
        """
        Créer une liste de résultats à partir d'un dictionnaire

        Args:
            json_data: Dictionnaire décrivant une liste de résultats

        Returns:
            Liste d'objets Results contenant les valeurs du dictionnaire, et exlucant les résultats sans valeur
        """
        results = []
        for item in json_data:
            country = item.get('country')
            name = item.get('name')

            result = cls()
            results.append(result)
        return results

    @classmethod
    def extract_results(cls, json_dict: dict) -> list[Results]:
        """
        Extrait les informations d'un dictionnaire json

        Args:
            json_dict: Dictionnaire représentant une liste d'objets Results
        Returns:
            Liste d'objet Results
        """
        return Results.from_json(json_dict[1])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Results'

        Returns:
            Objet Results sous forme de chaîne json
        """
        result_dict = {
            'countryiso3code': self.countryiso3code,
            'date': self.name,
        }
        return json.dumps(result_dict)
