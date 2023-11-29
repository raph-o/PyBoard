class ApiRoutes:
    BASE_URL = "https://api.worldbank.org/V2/fr"
    COUNTRIES = "/country"


class ApiPreferences:
    JSON_FORMAT = "format=json"

    @staticmethod
    def per_page(x: int) -> str:
        return "per_page=" + str(x)
