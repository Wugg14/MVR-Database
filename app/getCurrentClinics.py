from app.models import Clinic
"""Queries all the clinics and the database and return the serial number and company name
in a format that can be used as form options"""
def get_current_clinics():
    choices = []
    # query all the clinics currently in the DB
    allClinics = Clinic.query.all()
    # sort through them creating form choices with their name and serial number
    for c in allClinics:
        name = c.company
        serial = c.clinicSerialNum
        #create single string for the data processing in the route
        nameSerial = name + '__' + serial
        formattedChoice = (nameSerial, name)
        choices.append(formattedChoice)

    return choices
