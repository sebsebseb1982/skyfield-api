from dataclasses import dataclass, field

@dataclass
class Position:
    altitude:float = field()
    azimuth:float = field()
    distance:float = field()