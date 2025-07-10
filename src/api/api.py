from fastapi import FastAPI
from src.domain.position import Position
from src.domain.position_service import PositionService

app = FastAPI()
positionService:PositionService = PositionService()

@app.get("/position/{type}/{name}")
def get_position(type: str, name: str, latitude: float, longitude: float) -> Position:
    return positionService.get_position(type, name, latitude, longitude)

@app.get("/available-objects")
def get_objects():
    planets = load('de421.bsp')

    return {
        'planets-and-moons':planets.names()
    }