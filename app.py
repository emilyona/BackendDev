from flask import Flask, request
import dao
import json
from datetime import datetime
from db import db, Patient

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "Welcome to our Backend Development project!!"

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route("/api/patients/", methods=['GET'])
def get_patients():
    return success_response(dao.get_all_patients())

@app.route("/api/patients/", methods=['POST'])
def make_patient():
    body = json.loads(request.data)
    patient = dao.create_patient(
        name = body.get("name"),
        age = body.get("age")
    )
    return success_response(patient)

@app.route("/api/patients/<int:patient_id>/", methods=['GET'])
def get_patient_by_id(patient_id):
    patient = dao.get_patient_by_id(patient_id)
    if patient is not None:
        return success_response(patient)
    return failure_response("that patient does not exist!")

@app.route("/api/patients/<int:patient_id>/", methods=['DELETE'])
def delete_patient_by_id(patient_id):
    patient = dao.delete_patient_by_id(patient_id)
    if patient is not None:
        return success_response(patient)
    return failure_response("that patient does not exist!")

@app.route("/api/patients/<int:patient_id>/cycle/", methods=['GET'])
def ovulating(patient_id):
    patient = dao.get_patient_by_id(patient_id)
    if patient is None:
        return failure_response("that patient does not exist!")
    try:
        date = patient.last_cycle_date
    except Exception as e:
        return failure_response("that is not a valid date.")

    if dao.get_patient_by_id(patient_id) is None or date is None:
        return failure_response("Patient not found!")

    try:
        ov = dao.get_ovulation(date)
        if ov is True:
            return success_response("you are ovulating!")
        return success_response("you are not ovulating!")
    except Exception as e:
        return failure_response("that is not a valid date.")


@app.route("/api/patients/<int:patient_id>/cycle/", methods=['POST'])
def update_cycle(patient_id):
    patient = dao.get_patient_by_id(patient_id)
    if patient is None:
        return failure_response("that patient does not exist!")
    body = json.loads(request.data)
    last_cycle = body.get('last_cycle_date')
    try:
        patient = dao.update_cycle_by_id(patient_id,datetime.strptime(last_cycle, '%m-%d-%Y').date())
    except Exception as e:
        return failure_response("that is not a valid date.")
    return success_response(patient)

@app.route("/api/nurses/", methods=['GET'])
def get_nurses():
    return success_response(dao.get_all_nurses())

@app.route("/api/nurses/", methods=['POST'])
def make_nurse():
    body = json.loads(request.data)
    nurse = dao.create_nurse(
        name = body.get("name")
    )
    return success_response(nurse)

@app.route("/api/nurses/<int:nurse_id>/", methods=['GET'])
def get_nurse_by_id(nurse_id):
    nurse = dao.get_nurse_by_id(nurse_id)
    if nurse is not None:
        return success_response(nurse)
    return failure_response("that nurse does not exist!")

@app.route("/api/patients/<int:patient_id>/addnurse/", methods=['POST'])
def add_patient_to_nurse(patient_id):
    body = json.loads(request.data)
    patient = dao.add_patient(
        nurse_id = body.get('nurse_id'),
        patient_id = patient_id
    )
    if patient is not None:
        return success_response(patient)
    return failure_response("that patient or nurse does not exist!")

@app.route("/api/doctors/", methods=['GET'])
def get_doctors():
    return success_response(dao.get_all_doctors())

@app.route("/api/doctors/", methods=['POST'])
def make_doctor():
    body = json.loads(request.data)
    doctor = dao.create_doctor(
        name = body.get("name")
    )
    return success_response(doctor)

@app.route("/api/nurses/<int:nurse_id>/adddoctor/", methods=['POST'])
def add_nurse_to_doctor(nurse_id):
    body = json.loads(request.data)
    nurse = dao.add_nurse(
        doctor_id = body.get('doctor_id'),
        nurse_id = nurse_id
    )
    if nurse is not None:
        return success_response(nurse)
    return failure_response("that nurse or doctor does not exist!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
