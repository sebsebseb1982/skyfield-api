from skyfield.api import load, Topos, Star
from src.clients.simbad.simbad_repository import SimbadRepository
from src.domain.equatorial_coordinates import EquatorialCoordinates
from src.domain.horizontal_coordinates_service_exception import HorizontalCoordinatesServiceException
from src.domain.horizontal_coordinates import HorizontalCoordinates

class HorizontalCoordinatesService:
    def __init__(self, simbadRepository:SimbadRepository):
        self.simbadRepository=simbadRepository
        pass
    
    def get_horizontal_coordinates(self, type: str, name: str, latitude: float, longitude: float) -> HorizontalCoordinates:

        planets = load('de421.bsp')
        earth = planets['earth']
        # FIXME ajouter l'élévation
        observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)
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
        else:
            raise HorizontalCoordinatesServiceException()

