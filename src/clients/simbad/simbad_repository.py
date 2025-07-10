import requests
from src.domain.coordinates.equatorial_coordinates import EquatorialCoordinates


class SimbadRepository:
    def __init__(self):
        pass

    def get_equatorial_coordinates(self, objectName:str) -> EquatorialCoordinates:
        url = "https://simbad.u-strasbg.fr/simbad/sim-tap/sync"
        params = {
            "request": "doQuery",
            "lang": "adql",
            "format": "json",
            "query": f"SELECT main_id, ra, dec FROM basic WHERE main_id='{objectName}'"
        }

        response = requests.get(url, params=params)

        return EquatorialCoordinates(
            response.json()['data'][0][1],
            response.json()['data'][0][2]
        )