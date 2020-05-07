from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import dao


db = SQLAlchemy()

# many to many

association = db.Table("association", db.Model.metadata,
    db.Column("patient_id", db.Integer, db.ForeignKey("patients.id")),
    db.Column("nurse_id", db.Integer, db.ForeignKey("nurses.id"))
)

def update_cycle(self,id,cycle_time):
    self.conn.execute("""
        UPDATE patients
        SET last_cycle_date = ?
        WHERE id = ?;
    """, (cycle_time, id,))
    self.conn.commit()


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nurses = db.relationship('Nurse', secondary = association, back_populates='patients')
    last_cycle_date = db.Column(db.String)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.age = kwargs.get('age','')
        self.nurses = []
        self.last_cycle_date = None

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "nurses": [n.serialized() for n in self.nurses],
            "last_cycle_date": self.last_cycle_date
        }

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "last_cycle_date": self.last_cycle_date
        }
    


class Nurse(db.Model):
    __tablename__ = 'nurses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    patients = db.relationship('Patient', secondary = association, back_populates = 'nurses')
    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.patients = []
        self.doctor = ""

    def serialize(self):
        patients = []
        for p in self.patients:
            patients.append(p.serialized())

        doctorob = Doctor.query.filter_by(id=self.doctor).first()
        if doctorob is None:
            serialized_doctor = None
        else:
            serialized_doctor = doctorob.serialized()

        return {
            "id": self.id,
            "name": self.name,
            "patients": patients,
            "doctor": serialized_doctor
        }

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    def serialized_doc(self):
        patients = []
        for p in self.patients:
            patients.append(p.serialized())
        
        return {
            "id": self.id,
            "name": self.name,
            "patients": patients
        }

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    nurses = db.relationship('Nurse')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.nurses = []

    def serialize(self):
        nurses = []
        for n in self.nurses:
            nurses.append(n.serialized_doc())

        return {
            "id": self.id,
            "name": self.name,
            "nurses": nurses
        }

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name
        }