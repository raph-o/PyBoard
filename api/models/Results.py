from __future__ import annotations
import json
import pandas as pd
import api.Api
import api.models.Countries
import math


class Results:
    def __init__(self, country_code: str, country: str, value: float, date: str):
        self.country = country
        self.country_code = country_code
        self.value = value
        self.date = date

    @classmethod
    def from_json(cls, json_data: dict) -> list[Results]:
        results = []
        countries_list = api.Api.Api.get_countries()

        for item in json_data:
            country_code = item.get('countryiso3code')
            date = item.get('date')
            value = item.get('value')

            country_name = ""

            for country in countries_list:
                if country.code == country_code:
                    country_name = country.name
                    break
            if country_name != "":
                result = cls(country_code, country_name, value, date)
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
            'country_code': self.country_code,
            'country': self.country,
            'date': self.date,
            'value': self.value,
        }
        return json.dumps(result_dict)
