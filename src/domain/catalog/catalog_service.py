from src.domain.catalog.celestial_objects_collection import CelestialObject, CelestialObjectsCollection


class CatalogService:
    def __init__(self):
        pass

    def get_all(self) -> list[CelestialObjectsCollection]:
        pass
        return [
            CelestialObjectsCollection(
                'Planets & moons',
                'planets-and-moons',
                [
                    CelestialObject(
                        'Moon',
                        'moon'
                    ),
                    CelestialObject(
                        'Jupiter',
                        'jupiter'
                    ),
                    CelestialObject(
                        'Saturn',
                        'saturn'
                    ),
                    CelestialObject(
                        'Mars',
                        'mars'
                    )
                ]
            ),
            CelestialObjectsCollection(
                'Deep space',
                'deep-space-objects',
                [
                    CelestialObject(
                        'Whirpool Galaxy',
                        'm 51'
                    ),
                    CelestialObject(
                        'Polaris',
                        '* alf UMi'
                    )
                ]
            )
        ]