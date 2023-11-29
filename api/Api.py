import json
import requests
from api.ApiTools import *
from api.models.Results import Results


class Api:
    BASE_URL = ApiRoutes.BASE_URL
    url = ""

    def __init__(self, mode="standard"):
        self.mode = mode
        self.url = self.build_url()

    def build_url(self) -> str:
        url = (f"{self.BASE_URL}{ApiRoutes.COUNTRIES}/all/indicator/EN.ATM.GHGT.KT.CE?"
               f"{ApiPreferences.JSON_FORMAT}&"
               f"{ApiPreferences.per_page(1000)}")
        return url

    def get_result(self) -> str:
        response = requests.get(self.url)
        json_response = response.json()
        json_results = Results.extract_results(json_response)
        return json.dumps([json.loads(result.to_json()) for result in json_results])

    def get_specific_result(self, data_type: type):
        response = requests.get(self.url)
        json_response = response.json()
        extract_results = getattr(data_type, 'extract_results')
        json_results = extract_results(json_response)
        return json.dumps([json.loads(result.to_json()) for result in json_results])

