from __future__ import annotations

import json


class Countries:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    def __str__(self) -> str:
        return f'code: {self.code}, Name: {self.name}'

    @classmethod
    def from_json(cls, json_data: dict) -> list[Countries]:
        """
        Créer une liste de résultats à partir d'un dictionnaire

        Args:
            json_data: Dictionnaire décrivant une liste de résultats

        Returns:
            Liste d'objets Results contenant les valeurs du dictionnaire, et exlucant les résultats sans valeur
        """
        results = []
        for item in json_data[1]:
            code = item.get('id')
            name = item.get('name')
            if name != "":
                result = cls(code, name)
                results.append(result)
        return results

    @classmethod
    def extract_results(cls, json_dict: dict) -> list[Countries]:
        """
        Extrait les informations d'un dictionnaire json

        Args:
            json_dict: Dictionnaire représentant une liste d'objets Results
        Returns:
            Liste d'objet Results
        """
        return Countries.from_json(json_dict[1])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Results'

        Returns:
            Objet Results sous forme de chaîne json
        """
        result_dict = {
            'code': self.code,
            'name': self.name,
        }

        return json.dumps(result_dict)
