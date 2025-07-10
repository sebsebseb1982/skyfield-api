from fastapi import FastAPI
from src.clients.simbad.simbad_repository import SimbadRepository
from src.domain.catalog.catalog_service import CatalogService
from src.domain.coordinates.horizontal_coordinates import HorizontalCoordinates
from src.domain.coordinates.horizontal_coordinates_service import HorizontalCoordinatesService

app = FastAPI()
simbadRepository:SimbadRepository = SimbadRepository()
horizontalCoordinatesService:HorizontalCoordinatesService = HorizontalCoordinatesService(simbadRepository)
catalog_service:CatalogService = CatalogService()

@app.get("/horizontal-coordinates/{type}/{name}")
def get_position(type: str, name: str, latitude: float, longitude: float, elevation: float) -> HorizontalCoordinates:
    return horizontalCoordinatesService.get_horizontal_coordinates(type, name, latitude, longitude, elevation)

@app.get("/catalog")
def get_catalog():
    return catalog_service.get_all()