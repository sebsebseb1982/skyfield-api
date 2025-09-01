from skyfield.api import load, Topos, Star, wgs84
from src.clients.simbad.simbad_repository import SimbadRepository
from src.clients.wheretheiss.wheretheiss_repository import WhereTheISSRepository
from src.domain.coordinates.equatorial_coordinates import EquatorialCoordinates
from src.domain.coordinates.horizontal_coordinates import HorizontalCoordinates
from src.domain.coordinates.geographic_coordinates import GeographicCoordinates
from src.domain.coordinates.horizontal_coordinates_service_exception import HorizontalCoordinatesServiceException

class HorizontalCoordinatesService:
    def __init__(self, simbadRepository:SimbadRepository, whereTheISSRepository:WhereTheISSRepository):
        self.simbadRepository=simbadRepository
        self.whereTheISSRepository=whereTheISSRepository
        pass
    
    def get_horizontal_coordinates(self, type: str, name: str, latitude: float, longitude: float, elevation: float) -> HorizontalCoordinates:

        planets = load('de421.bsp')
        earth = planets['earth']
        observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude, elevation_m=elevation)
        ts = load.timescale()
        t = ts.now()

        if(type=='planets-and-moons'):
            target = planets[name]

            astrometric = observer.at(t).observe(target)
            alt, az, distance = astrometric.apparent().altaz()

            return HorizontalCoordinates(
                alt.degrees,
                az.degrees,
                distance.km
            )
        elif(type=='deep-space-objects'):
            equatorialCoordinates: EquatorialCoordinates = self.simbadRepository.get_equatorial_coordinates(name)
            star = Star(ra_hours=equatorialCoordinates.right_ascension / 15.0, dec_degrees=equatorialCoordinates.declination)

            astrometric = observer.at(t).observe(star).apparent()
            alt, az, distance = astrometric.altaz()

            return HorizontalCoordinates(
                alt.degrees,
                az.degrees,
                distance.km
            )
        elif(type=='specials' and name=='iss'):
            issCoordinates: GeographicCoordinates = self.whereTheISSRepository.get_iss_geographic_coordinates()

            observer = wgs84.latlon(
                latitude,
                longitude,
                elevation_m=elevation
            ).at(t)

            # -----------------------------------
            # 2. Définir la position de l’ISS (lat/lon/alt connus à t)
            # -----------------------------------
            iss_lat = 50.0       # latitude ISS (°)
            iss_lon = 10.0       # longitude ISS (°)
            iss_alt = 408000     # altitude ISS (mètres, ~408 km)

            iss_position = wgs84.latlon(
                issCoordinates.latitude,
                issCoordinates.longitude,
                elevation_m=issCoordinates.altitude * 1000
            ).at(t)

            # ---------------------------------------------------
            # 3. Calcul du vecteur topocentrique (ISS vu depuis l’observateur)
            # ---------------------------------------------------
            topocentric = iss_position - observer

            alt, az, distance = topocentric.altaz()

            return HorizontalCoordinates(
                alt.degrees,
                az.degrees,
                distance.km
            )
        else:
            raise HorizontalCoordinatesServiceException()

