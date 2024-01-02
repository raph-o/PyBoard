from __future__ import annotations

import json


"""
Objet information présent dans toutes les réponses json que renvoie l'api.
Cet objet a été le premier afin de prototyper le projet et travailler sur les autres aspects du dashnoard en parallèle.
Exemple de ce renvois l'api sous forme de json :
{
    "page": 1,
    "pages": 1,
    "per_page": "300",
    "total": 297
}
N'importe quelle requête disponible dans les autres classes modèle permet de récupérer un tel objet
"""
class Information:
    def __init__(self, page: int, pages: int, per_page: int, total: int, source_id: str, last_updated: str) -> None:
        self.page = page
        self.pages = pages
        self.per_page = per_page
        self.total = total
        self.source_id = source_id
        self.last_updated = last_updated

    def __str__(self) -> str:
        return f'Page: {self.page}, Pages: {self.pages}, Per Page: {self.per_page}, Total: {self.total}, Source ID: {self.sourceid}, Last Updated: {self.lastupdated}'

    @classmethod
    def from_json(cls, json_data: dict) -> Information:
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
    def extract_information(cls, json_dict: dict) -> Information:
        """
        Extrait les informations d'un dictionnaire json

        Args:
            json_dict: Dictionnaire représentant un objet Informations
        Returns:
            Objet Informations
        """
        return Information.from_json(json_dict[0])

    def to_json(self) -> str:
        """
        Créer une représentation json de l'objet Informations

        Returns:
            Objet Informations sous forme de chaîne json
        """
        information_dict = {
            'page': self.page,
            'pages': self.pages,
            'per_page': self.per_page,
            'total': self.total,
            'sourceid': self.source_id,
            'lastupdated': self.last_updated
        }

        return json.dumps(information_dict)
