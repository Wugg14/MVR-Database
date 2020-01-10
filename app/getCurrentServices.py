from app.models import MiscService
"""Queries all the services in the database and returns the service name
in a format that can be used as form options"""
def get_current_services():
    choices = []
    allServices = MiscService.query.all()
    for s in allServices:
        name = (s.serviceType, s.serviceType)
        choices.append(name)

    return choices
