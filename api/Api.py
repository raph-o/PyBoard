import json
import requests

import api
from api.models import Countries, GreenhouseGases, Results
from api.ApiTools import *


class Api:
    def __init__(self, mode="standard"):
        self.mode = mode

    @staticmethod
    def get_result() -> str:
        response = requests.get(ApiEndPoints.RESULTS)
        json_response = response.json()
        json_results = api.models.Results.Results.extract_results(json_response)
        return json.dumps([json.loads(result.to_json()) for result in json_results])

    @staticmethod
    def get_countries():
        response = requests.get(ApiEndPoints.COUNTRIES)
        json_response = response.json()
        json_results = api.models.Countries.Countries.from_json(json_response)
        return json_results
