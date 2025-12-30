from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date


# PATIENT TABLE 

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=30)
    age: int
    gender: str = Field(max_length=8)
    phone: str = Field(max_length=10)
    place: str = Field(max_length=20)
    admission_date: date
    doctor_name: str = Field(max_length=20)
    status: str = Field(default="Active")


# DOCTOR TABLE

class Doctor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=20)
    specialty: str = Field(max_length=30)
    phone: str = Field(max_length=10)