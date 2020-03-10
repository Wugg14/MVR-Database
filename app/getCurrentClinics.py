from app.models import Clinic
from app.structureSelectFields import structure_options
"""Queries all the clinics in the database and return the serial number and company name
in a format that can be used as form options"""
def get_current_clinics():
    choices = []
    # query all the clinics currently in the DB
    allClinics = Clinic.query.all()
    # sort through them creating form choices with their name and serial number
    for c in allClinics:
        name = c.company
        serial = c.clinicSerialNum
        formattedChoice = structure_options(name, serial)
        choices.append(formattedChoice)

    return choices
