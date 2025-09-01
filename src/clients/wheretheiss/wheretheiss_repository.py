import requests
from src.domain.coordinates.geographic_coordinates import GeographicCoordinates


class WhereTheISSRepository:
    def __init__(self):
        pass

    def get_iss_geographic_coordinates(self) -> GeographicCoordinates:
        url = "https://api.wheretheiss.at/v1/satellites/25544"

        response = requests.get(url, params={})

        return GeographicCoordinates(
            latitude=response.json()['latitude'],
            longitude=response.json()['longitude'],
            altitude=response.json()['altitude']
        )