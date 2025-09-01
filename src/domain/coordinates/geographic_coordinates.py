from dataclasses import dataclass, field

@dataclass
class GeographicCoordinates:
    latitude:float = field()
    longitude:float = field()
    altitude:float = field()