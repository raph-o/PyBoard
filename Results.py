from __future__ import annotations

import json


class Results:
    def __init__(self, countryiso3code: str, date: str, value: float):
        self.countryiso3code = countryiso3code
        self.date = date
        self.value = value

    def __str__(self) -> str:
        return f'Country3isocode: {self.countryiso3code}, Date: {self.date}, Value: {self.value}'

    @classmethod
    def from_json(cls, json_data: dict) -> list:
        results = []
        for item in json_data:
            countryiso3code = item.get('countryiso3code')
            date = item.get('date')
            value = item.get('value')
            result = cls(countryiso3code, date, value)
            results.append(result)
        return results

    @classmethod
    def extract_results(cls, json_dict: dict) -> list:
        return Results.from_json(json_dict[1])

    def to_json(self) -> str:
        result_dict = {
            'countryiso3code': self.countryiso3code,
            'date': self.date,
            'value': self.value
        }

        return json.dumps(result_dict)
