from db import db, Patient, Nurse, Doctor
from datetime import datetime
from datetime import timedelta

# your methods here
def get_all_patients():
    return [p.serialize() for p in Patient.query.all()]

def create_patient(name, age):
    new_patient = Patient(
        name = name,
        age = age
    )
    db.session.add(new_patient)
    db.session.commit()
    return new_patient.serialize()

def get_patient_by_id(patient_id):
    patient=Patient.query.filter_by(id=patient_id).first()
    if patient is None:
        return None
    return patient.serialize()

def delete_patient_by_id(patient_id):
    patient = Patient.query.filter_by(id=patient_id).first()
    if patient is None:
        return None
    db.session.delete(patient)
    db.session.commit()
    return patient.serialize()

def update_cycle_by_id(patient_id, cycle_time):
    patient = Patient.query.filter_by(id=patient_id).first()
    if patient is None:
        return None
    patient.last_cycle_date = cycle_time
    db.session.commit()
    return patient.serialize()

def days_between(start, today):
    if (today - start).days < 0:
        return None
    return (today - start).days

def get_ovulation(startDate):
    start = datetime.strptime(startDate, '%Y-%m-%d').date()
    today = datetime.today().date()
    days = days_between(start,today)
    if days >28:
        days = days_between(start+timedelta(days = 28),today)
    if days <=16 and days >=12:
        return True
    return False

#nurses

def get_all_nurses():
    return [n.serialize() for n in Nurse.query.all()]

def create_nurse(name):
    new_nurse = Nurse(
        name = name
    )

    db.session.add(new_nurse)
    db.session.commit()
    return new_nurse.serialize()

def get_nurse_by_id(nurse_id):
    nurse=Nurse.query.filter_by(id=nurse_id).first()
    if nurse is None:
        return None
    return nurse.serialize()

def delete_nurse_by_id(nurse_id):
    nurse=Nurse.query.filter_by(id=nurse_id).first()
    if nurse is None:
        return None
    db.session.delete(nurse)
    db.session.commit()
    return nurse.serialize()

def add_patient(nurse_id, patient_id):
    nurse = Nurse.query.filter_by(id=nurse_id).first()
    patient = Patient.query.filter_by(id=patient_id).first()
    if nurse is None or patient is None:
        return None
    nurse.patients.append(patient)

    db.session.commit()
    return patient.serialize()

#doctors

def get_all_doctors():
    return [d.serialize() for d in Doctor.query.all()]

def create_doctor(name):
    new_doctor = Doctor(
        name = name
    )
    db.session.add(new_doctor)
    db.session.commit()
    return new_doctor.serialize()


def add_nurse(doctor_id, nurse_id):
    nurse = Nurse.query.filter_by(id=nurse_id).first()
    doctor = Doctor.query.filter_by(id=doctor_id).first()
    if nurse is None or doctor is None:
        return None
    doctor.nurses.append(nurse)

    db.session.commit()
    return nurse.serialize()
