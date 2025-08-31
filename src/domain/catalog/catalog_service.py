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
                        'Sun',
                        'sun'
                    ),
                    CelestialObject(
                        'Jupiter',
                        'jupiter barycenter'
                    ),
                    CelestialObject(
                        'Saturn',
                        'saturn barycenter'
                    ),
                    CelestialObject(
                        'Mars',
                        'mars'
                    ),
                    CelestialObject(
                        'Mercury',
                        'mercury'
                    ),
                    CelestialObject(
                        'Venus',
                        'venus'
                    ),
                    CelestialObject(
                        'Uranus',
                        'uranus barycenter'
                    ),
                    CelestialObject(
                        'Pluto',
                        'pluto'
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
            ),
            CelestialObjectsCollection(
                'Specials',
                'specials',
                [
                    CelestialObject(
                        'International Space Station',
                        'iss'
                    )
                ]
            )
        ]