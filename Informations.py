import json


class Informations:
    def __init__(self, page: int, pages: int, per_page: int, total: int, sourceid: str, lastupdated: str):
        self.page = page
        self.pages = pages
        self.per_page = per_page
        self.total = total
        self.sourceid = sourceid
        self.lastupdated = lastupdated

    def __str__(self):
        return f"Page: {self.page}, Pages: {self.pages}, Per Page: {self.per_page}, Total: {self.total}, Source ID: {self.sourceid}, Last Updated: {self.lastupdated}"

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(
            json_data['page'],
            json_data['pages'],
            json_data['per_page'],
            json_data['total'],
            json_data['sourceid'],
            json_data['lastupdated']
        )

    @classmethod
    def extract_informations(cls, json_response: dict):
        return Informations.from_json(json_response[0])

    def to_json(self) -> str:
        informations_dict = {
            'page': self.page,
            'pages': self.pages,
            'per_page': self.per_page,
            'total': self.total,
            'sourceid': self.sourceid,
            'lastupdated': self.lastupdated
        }

        return json.dumps(informations_dict)
