class ApiRoutes:
    BASE_URL = "https://api.worldbank.org/V2/fr"
    COUNTRIES = "/country"


class ApiPreferences:
    JSON_FORMAT = "format=json"

    @staticmethod
    def per_page(x: int) -> str:
        return "per_page=" + str(x)


class ApiEndPoints:
    RESULTS = (f"{ApiRoutes.BASE_URL}{ApiRoutes.COUNTRIES}/all/indicator/EN.ATM.GHGT.KT.CE?"
               f"{ApiPreferences.JSON_FORMAT}&"
               f"{ApiPreferences.per_page(1000)}")
    COUNTRIES = (f"{ApiRoutes.BASE_URL}{ApiRoutes.COUNTRIES}?"
                 f"{ApiPreferences.JSON_FORMAT}&"
                 f"{ApiPreferences.per_page(500)}")
