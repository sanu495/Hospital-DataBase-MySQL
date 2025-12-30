from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from typing import List, Optional
from database import create_db_and_tables, get_session, engine
from schema import Patient, Doctor

router =APIRouter()

templates = Jinja2Templates(directory="static")


@router.get("/", name="home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html",{"request":request})

@router.get("/Dashboard", name="dash_board", response_class=HTMLResponse)
def details(request: Request, session: Session = Depends(get_session)):
    patients_count = session.exec(select(Patient)).count()
    doctors_count = session.exec(select(Doctor)).count()

    return templates.TemplateResponse("dashboard.html", {"request":request, "patients":patients_count, "doctors":doctors_count})

@router.get("/Patients", response_class=HTMLResponse)
def get_patients(request: Request, session: Session = Depends(get_session)):
    patients = session.exec(select(Patient)).all()

    return templates.TemplateResponse("patients.html", {"request":request, "patients":patients})
