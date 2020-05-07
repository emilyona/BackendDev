Rebekah Westerlind, Emily Sine

NetIDs: rw537, ejs345

# Backend Final Project API Specification
Due Date: Sunday, May 10

## Get all patients

```
GET /api/patients/
```
Response
    
    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Bonnie",
                "age": 34,
                "nurses": [<SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "last_cycle_date": <USER INPUT>
            },
            {
                "id": 2,
                "name": "Sally",
                "age": 4,
                "nurses": [<SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "last_cycle_date": <USER INPUT>
            },
            ...
        ]
    }



## Create a patient
```
POST /api/patients/
```
Request

    {
        "name": <USER INPUT>,
        "age": <USER INPUT>
    }
    
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "age": <USER INPUT>
                "nurses": [],
                "last_cycle_date": None
        }
    }

## Get a specific patient
```
GET /api/patients/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "age": <USER INPUT>,
                "nurses":  [<SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "last_cycle_date": <USER INPUT>
        }
    }


## Delete a specific patient
```
DELETE /api/patients/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "age": <USER INPUT>,
                "nurses":  [<SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "last_cycle_date": <USER INPUT>
        }
    }
   
## Update cycle
```
POST /api/patients/{id}/cycle/
```
Request

    {
        "last_cycle_date": <USER INPUT>
    }
    
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "age": <USER INPUT>,
                "nurse": [<SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "last_cycle_date": <USER INPUT>
        }
    }
    

## Get all nurses
```
GET /api/nurses/
```
Response

    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Franny",
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
                "doctor": ""
            },
            {
                "id": 2,
                "name": "Bob",
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
                "doctor": ""
            },
            ...
        ]
    }

## Create a specific nurse
```
POST /api/nurses/
```
Request

    {
        "name": <USER INPUT>
    }
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
                "doctor": ""
        }
    }

## Get a specific nurse
```
GET /api/nurses/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
                "doctor": ""
        }
    }
## Assign a patient to a nurse
```
POST /api/patients/{id}/addnurse/
```
Request

    {
        "nurse_id": <USER INPUT>
    }

Response

    {
        "success": true,
        "data": <SERIALIZED PATIENT>
    }    
    
## Get all doctors
```
GET /api/doctors/
```
Response

    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Franny",
                "nurses": [ <SERIALIZED NURSE WITHOUT DOCTOR FIELD,...>]
            },
            {
                "id": 2,
                "name": "Bob",
                "nurses": [ <SERIALIZED NURSE WITHOUT DOCTOR FIELD,...>]
            },
            ...
        ]
    }

## Create a doctor
```
POST /api/doctors/
```
Request

    {
        "name": <USER INPUT>
    }
    
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "nurses": []
        }
    }


## Assign a nurse to a doctor
```
POST /api/nurses/{id}/adddoctor/
```
Request

    {
        "doctor_id": <USER INPUT>
    }

Response

    {
        "success": true,
        "data": <SERIALIZED NURSE>
    }    

