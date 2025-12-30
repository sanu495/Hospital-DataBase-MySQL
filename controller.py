from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from database import get_session
from schema import Patient, Doctor
from datetime import date

router =APIRouter()

templates = Jinja2Templates(directory="static")


# HOME PAGE

@router.get("/", name="home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html",{"request":request})

@router.get("/Form", name="create_form", response_class=HTMLResponse)
def get_form(request:Request):
    return templates.TemplateResponse("form.html", {"request":request})


# DASHBOARD


@router.get("/Dashboard", name="dash_board", response_class=HTMLResponse)
def details(request: Request, session: Session = Depends(get_session)):
    patients_count = len(session.exec(select(Patient)).all())
    doctors_count = len(session.exec(select(Doctor)).all())

    return templates.TemplateResponse("dashboard.html", {"request":request, "patients":patients_count, "doctors":doctors_count})


# PATIENTS AND DOCTORS DETAILS 


@router.get("/Patients", name="patient_details", response_class=HTMLResponse)
def get_patients(request: Request, session: Session = Depends(get_session)):
    patients = session.exec(select(Patient)).all()

    return templates.TemplateResponse("patients.html", {"request":request, "patients":patients})

@router.get("/Doctors", name="doctor_details", response_class=HTMLResponse)
def get_doctors(request:Request, session: Session = Depends(get_session)):
    doctors = session.exec(select(Doctor)).all()

    return templates.TemplateResponse("doctors.html", {"request":request, "doctors":doctors})


# CREATE PATIENT DETAIL


@router.post("/patients/create", response_class=HTMLResponse)
def create_patient_form_post(request: Request, name: str = Form(...), age: int = Form(...), gender: str = Form(...),
                             phone: str = Form(...), place: str = Form(...), admission_date: date = Form(...), 
                             doctor_name: str = Form(...), status: str = Form(...), session: Session = Depends(get_session)):
        
    db_patient = Patient(
        name=name,
        age=age,
        gender=gender,
        phone=phone,
        place=place,
        admission_date=admission_date,
        doctor_name=doctor_name,
        status=status)
    
    session.add(db_patient)
    session.commit()
    session.refresh(db_patient)
    patients = session.exec(select(Patient)).all()
    return templates.TemplateResponse("patients.html", {"request": request, "patients":patients})
