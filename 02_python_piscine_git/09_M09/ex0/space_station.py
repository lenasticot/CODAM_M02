from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)
    
def main():
    print("Space Station Data Validation")
    print()
    print("Valid station created:")
    try:
        valid_test = SpaceStation.model_validate({
            "station_id": "Baguette",
            "name": "Lt. Reblochon",
            "crew_size": 5,
            "power_level": 1.5,
            "oxygen_level": 3.3,
            "last_maintenance": "2024-01-15",
            "is_operational": True,
            "notes": "Un regiment de fromage blanc, déclare la guerre aux camemberts"
        })
        print(f"ID: {valid_test.station_id}")
        print(f"Name: {valid_test.name}")
        print(f"Crew: {valid_test.crew_size} people")
        print(f"Power: {valid_test.power_level}%")
        print(f"Oxygen: {valid_test.oxygen_level}%")
        print(f"Status: {'Operational' if valid_test.is_operational else 'Offline'}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
    print()
    try:
        invalid = SpaceStation.model_validate({
                "station_id": "BaguetteDelEspace",
                "name": "Lt. ReblochonQuiAEteOublieAuFondDuFrigoDoncPasSurMaisBonCaSeTenteQuandMeme",
                "crew_size": 50,
                "power_level": 80.5,
                "oxygen_level": 120.3,
                "last_maintenance": "2024-01-15",
                "is_operational": True,
                "notes": "Un regiment de fromage blanc, déclare la guerre aux camemberts"
        })
        print(f"ID: {invalid.station_id}")
        print(f"Name: {invalid.name}")
        print(f"Crew: {invalid.crew_size} people")
        print(f"Power: {invalid.power_level}%")
        print(f"Oxygen: {invalid.oxygen_level}%")
        print(f"Status: {'Operational' if invalid.is_operational else 'Offline'}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
main()
