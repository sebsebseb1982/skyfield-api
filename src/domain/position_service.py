from skyfield.api import load, Topos
from src.domain.position import Position

class PositionService:
    def __init__(self):
        pass
    
    def get_position(self, type: str, name: str, latitude: float, longitude: float) -> Position:
        ts = load.timescale()
        t = ts.now()
        planets = load('de421.bsp')
        earth = planets['earth']
        target = planets[name]

        observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)

        astrometric = observer.at(t).observe(target)
        alt, az, distance = astrometric.apparent().altaz()

        return Position(
            alt.degrees,
            az.degrees,
            distance.km
        )