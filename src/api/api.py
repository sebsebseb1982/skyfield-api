from fastapi import FastAPI
from src.clients.simbad.simbad_repository import SimbadRepository
from src.domain.horizontal_coordinates import HorizontalCoordinates
from src.domain.horizontal_coordinates_service import HorizontalCoordinatesService

app = FastAPI()
simbadRepository:SimbadRepository = SimbadRepository()
horizontalCoordinatesService:HorizontalCoordinatesService = HorizontalCoordinatesService(simbadRepository)

@app.get("/horizontal-coordinates/{type}/{name}")
def get_position(type: str, name: str, latitude: float, longitude: float, elevation: float) -> HorizontalCoordinates:
    return horizontalCoordinatesService.get_horizontal_coordinates(type, name, latitude, longitude, elevation)

@app.get("/catalog")
def get_objects():
    planets = load('de421.bsp')

    return {
        'planets-and-moons':planets.names()
    }