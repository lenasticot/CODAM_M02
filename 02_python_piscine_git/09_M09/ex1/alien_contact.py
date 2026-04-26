from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional

class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

class AlienContact(BaseModel):
    contact_id : str = Field(min_length=5, max_length=15)
    timestamp : datetime
    location : str = Field(min_length=3, max_length=100)
    contact_type : ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False
    
    @model_validator(mode="after")
    def check_name(self):
        if self.contact_id.startswith("AC"):
            return self
        else:
            raise ValueError("Contact id must start with AC")
    
    @model_validator(mode="after")
    def check_physical(self):
        if self.contact_type == ContactType.physical:
            if self.is_verified == False:
                raise ValueError("Physical contacts must be verified")
            else:
                return self
        elif self.contact_type == ContactType.telepathic:
            if self.witness_count >= 3:
                return self
            else:
                raise ValueError("Telepathic contacts must have at least 3 witnesses")
        return self
    
    @model_validator(mode="after")
    def check_signal(self):
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Signal strength above 7.0 must have a received message")
            else:
                return self
        return self


def main():
    print("Alien Contact Log Validation")
    print()
    try:
        valid = AlienContact.model_validate({
            "contact_id": "AC-bonjour",
            "timestamp": "2024-01-18",
            "location": "ton cul",
            "contact_type": "visual",
            "signal_strength": 5.0,
            "duration_minutes": 35,
            "witness_count": 12,
            "message_received": "Si t'as un gros cul, t'as tout ce que j'aime",
            "is_verified": False,
        })
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.value}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: {valid.message_received}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
    print()
    try:
        invalid = AlienContact.model_validate({
            "contact_id": "bonjour",
            "timestamp": "2024-01-18",
            "location": "ton cul",
            "contact_type": "visual",
            "signal_strength": 5.0,
            "duration_minutes": 35,
            "witness_count": 12,
            "message_received": "Si t'as un gros cul, t'as tout ce que j'aime",
            "is_verified": False,
        })
        print(invalid)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])

main()
