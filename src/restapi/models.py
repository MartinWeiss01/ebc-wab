from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime

class Bed(BaseModel):
    type: str

class MedicalExamination(BaseModel):
    datetime: datetime
    doctor: str
    report: str

class Pet(BaseModel):
    id: UUID
    name: str
    registration: date | None
    bed: Bed | None
    medical_examination: list[MedicalExamination] | None