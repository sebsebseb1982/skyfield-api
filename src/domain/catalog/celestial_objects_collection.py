from dataclasses import dataclass, field

@dataclass
class CelestialObject:
    label:str = field()
    code:str = field()

@dataclass
class CelestialObjectsCollection:
    label:str = field()
    code:str = field()
    objects:list[CelestialObject] = field()