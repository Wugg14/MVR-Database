from app.models import MiscService
"""Queries all the services in the database and returns the service name
in a format that can be used as form options"""
def get_current_services():
    choices = []
    allServices = MiscService.query.all()
    for s in allServices:
        name = s.serviceType
        price = s.servicePrice
        price = str(price)
        namePrice = name + '__' + price
        formattedChoice = (namePrice, name)
        choices.append(formattedChoice)

    return choices
