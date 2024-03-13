from dataclasses import dataclass
from typing import Optional


@dataclass
class VacancyDTO:
    company: str
    title: str
    location: str
    description: str
    technologies: list[str]
    salary: Optional[str]
    english: Optional[str]
    years_of_experience: int
    employment_type: Optional[str]
    views: int
    appliances: int
