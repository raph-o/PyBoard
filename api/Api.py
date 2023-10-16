from api.Results import Results
import json
import requests


class Api:
    BASE_URL = "https://api.worldbank.org/V2/fr/"
    url = ""
    params = {"format": "json", "per_page": "1000"}

    def __init__(self, mode="standard", resp_format="json", resp_per_page="1000"):
        self.mode = mode
        self.params["format"] = resp_format
        self.params["per_page"] = resp_per_page
        self.url = self.build_url()

    def build_url(self) -> str:
        url = (f"{self.BASE_URL}country/all/indicator/EN.ATM.GHGT.KT.CE?format={self.params['format']}&per_page"
               f"={self.params['per_page']}")
        return url

    def get_result(self) -> str:
        response = requests.get(self.url)
        json_response = response.json()
        json_results = Results.extract_results(json_response)
        return json.dumps([json.loads(result.to_json()) for result in json_results])
