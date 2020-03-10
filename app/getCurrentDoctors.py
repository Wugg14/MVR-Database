from app.models import Doctor
from app.structureSelectFields import structure_options
"""Queries all the clinics and the database and return the serial number and company name
in a format that can be used as form options"""
def get_current_doctors():
    choices = []
    # query all the clinics currently in the DB
    allDocs = Doctor.query.all()
    # sort through them creating form choices with their name and serial number
    for d in allDocs:
        name = d.first + ' ' + d.last
        serial = d.doctorSerialNum
        formattedChoice = structure_options(name, serial)
        choices.append(formattedChoice)

    return choices
