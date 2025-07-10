from dataclasses import dataclass, field

@dataclass
class HorizontalCoordinates:
    altitude:float = field()
    azimuth:float = field()
    distance:float = field()