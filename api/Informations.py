from __future__ import annotations

import json


class Informations:
    def __init__(self, page: int, pages: int, per_page: int, total: int, sourceid: str, lastupdated: str) -> None:
        self.page = page
        self.pages = pages
        self.per_page = per_page
        self.total = total
        self.sourceid = sourceid
        self.lastupdated = lastupdated

    def __str__(self) -> str:
        return f'Page: {self.page}, Pages: {self.pages}, Per Page: {self.per_page}, Total: {self.total}, Source ID: {self.sourceid}, Last Updated: {self.lastupdated}'

    @classmethod
    def from_json(cls, json_data: dict) -> Informations:
        """
        Créer un objet Informations à partir d'un dictionnaire

        Args:
            json_data: Dictionnaire décrivant un objet Informations et ses valeurs

        Returns:
            Objet Informations contenant les valeurs contenues dans le dictionnaire
        """
        return cls(
            json_data['page'],
            json_data['pages'],
            json_data['per_page'],
            json_data['total'],
            json_data['sourceid'],
            json_data['lastupdated']
        )

    @classmethod
    def extract_informations(cls, json_dict: dict) -> Informations:
        """
        Extrait les informations d'un dictionnaire json

        Args:
            json_dict: Dictionnaire représentant un objet Informations
        Returns:
            Objet Informations
        """
        return Informations.from_json(json_dict[0])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Informations

        Returns:
            Objet Informations sous forme de chaîne json
        """
        informations_dict = {
            'page': self.page,
            'pages': self.pages,
            'per_page': self.per_page,
            'total': self.total,
            'sourceid': self.sourceid,
            'lastupdated': self.lastupdated
        }

        return json.dumps(informations_dict)
