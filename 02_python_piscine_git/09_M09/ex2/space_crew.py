from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional

class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def id_check(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with a 'M'")
        return self
    @model_validator(mode="after")
    def rank_check(self):
        i = 0
        for crewmember in self.crew:
            if crewmember.rank.value == "captain":
                i +=1
            elif crewmember.rank.value == "commander":
                i +=1
        if i >= 1:
            return self
        else:
            raise ValueError("You need at least one commander or captain for this space mission")
    @model_validator(mode="after")
    def long_mission(self):
        if self.duration_days > 365:
            i = 0
            for crewmember in self.crew:
                if crewmember.years_experience >= 5:
                    i += 1
            if i / len(self.crew) < 0.5:
                raise ValueError("At least 50%% of the crew must have 5 years of experience for a trip that long")
            else:
                return self
        return self
    @model_validator(mode="after")
    def active_members(self):
        inactive = [member.name for member in self.crew if not member.is_active]
        if inactive:
                raise ValueError(f"Inactive crew members: {', '.join(inactive)}")
        return self