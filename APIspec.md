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
                "nurse": <SERIALIZED NURSE WITHOUT PATIENT FIELD>,
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ],
                "last_cycle_date": <USER INPUT>
            },
            {
                "id": 2,
                "name": "Sally",
                "age": 4,
                "nurse": <SERIALIZED NURSE WITHOUT PATIENT FIELD>,
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ],
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
                "nurse": None,
                "hormones": [],
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
                "nurse":  <SERIALIZED NURSE WITHOUT PATIENT FIELD>,
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
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
                "nurse":  <SERIALIZED NURSE WITHOUT PATIENT FIELD>,
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
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
                "nurse": <SERIALIZED NURSE WITHOUT PATIENT FIELD>,
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ],
                "last_cycle_date": <USER INPUT>
        }
    }
    
## Check cycle
```
GET /api/patients/{id}/cycle/
```

    
Response

    {
        "success": true,
        "data": "low", "medium" or "high"
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
            },
            {
                "id": 2,
                "name": "Bob",
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
            },
            ...
        ]
    }

## Get a specific nurses
```
GET /api/nurses/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>]
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

## Get all hormones
```
GET /api/hormones/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>
        }
    }

## Assign a hormone to a patient
```
POST /api/patients/{id}/addhormone/
```
Request

    {
        "hormone_id": <USER INPUT>
    }

Response

    {
        "success": true,
        "data": <SERIALIZED PATIENT>
    }   



