import json
import requests

import api
from api.models import Countries, Results
from api.ApiTools import *


"""
Classe permettant de contruire le jeu de données utilisé par le dashboard
"""
class Api:
    def __init__(self, mode="standard"):
        self.mode = mode

    @staticmethod
    def get_result() -> str:
        """
        Créer une chaîne de caractère json représentant notre jeu de données entier
        :return: Une chaîne de caractère json
        """
        response = requests.get(ApiEndPoints.RESULTS)
        json_response = response.json()
        json_results = api.models.Results.Results.extract_results(json_response)
        return json.dumps([json.loads(result.to_json()) for result in json_results])

    @staticmethod
    def get_countries():
        """
        Récupère des informations sur les différents pays proposés par l'api
        :return: Liste d'objet pays
        """
        response = requests.get(ApiEndPoints.COUNTRIES)
        json_response = response.json()
        json_results = api.models.Countries.Countries.from_json(json_response)
        return json_results
