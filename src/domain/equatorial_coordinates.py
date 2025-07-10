from dataclasses import dataclass, field

@dataclass
class EquatorialCoordinates:
    right_ascension:float = field()
    declination:float = field()