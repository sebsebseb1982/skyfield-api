from fastapi import FastAPI
from skyfield.api import load, Topos


app = FastAPI()

@app.get("/position/{type}/{name}")
def get_position(type: str, name: str, latitude: float, longitude: float):
    ts = load.timescale()
    t = ts.now()
    planets = load('de421.bsp')
    earth = planets['earth']
    target = planets[name]

    observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    astrometric = observer.at(t).observe(target)
    alt, az, distance = astrometric.apparent().altaz()

    return {
        "body": f"{type}/{name}",
        "altitude": alt.degrees,
        "azimuth": az.degrees,
        "distance": distance.km
    }

@app.get("/available-objects")
def get_objects():
    planets = load('de421.bsp')

    return {
        'planets-and-moons':planets.names()
    }