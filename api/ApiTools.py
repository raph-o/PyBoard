"""
Classe contenant des constantes communes à l'api, utilisées pour créer une url de base
"""
class ApiRoutes:
    BASE_URL = "https://api.worldbank.org/V2/fr"
    COUNTRIES = "/country"


"""
Classe contenant des constances communes à l'api afin d'ajouter des paramètres à la requête
"""
class ApiPreferences:
    JSON_FORMAT = "format=json"

    @staticmethod
    def per_page(x: int) -> str:
        """
        Fonction permettant de créer le paramètre de requête per_page dynamiquement
        :param x: nombre d'éléments voulus par page
        :return: une chaîne de caractère indiquant le nombre d'éléments que l'on veut par page
        """
        return "per_page=" + str(x)


"""
Classe listant les différents endpoints que l'on utilise pour construire notre jeu de données
"""
class ApiEndPoints:
    RESULTS = (f"{ApiRoutes.BASE_URL}{ApiRoutes.COUNTRIES}/all/indicator/EN.ATM.GHGT.KT.CE?"
               f"{ApiPreferences.JSON_FORMAT}&"
               f"{ApiPreferences.per_page(16758)}")
    COUNTRIES = (f"{ApiRoutes.BASE_URL}{ApiRoutes.COUNTRIES}?"
                 f"{ApiPreferences.JSON_FORMAT}&"
                 f"{ApiPreferences.per_page(500)}")
