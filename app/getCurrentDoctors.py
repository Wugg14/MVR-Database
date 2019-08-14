from app.models import Doctor
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
        #create single string for the data processing in the route
        nameSerial = name + '__' + serial
        formattedChoice = (nameSerial, name)
        choices.append(formattedChoice)

    return choices
