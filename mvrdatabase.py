from app import app, db
from app.models import User, Clinic, Doctor, Report_US, Report_Radiographic, Report_CT, MiscService, Report_Misc, Report_Echo

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Clinic': Clinic, 'Doctor': Doctor, 'Report_US': Report_US, 'Report_Radiographic': Report_Radiographic, 'Report_CT': Report_CT, 'MiscService': MiscService, 'Report_Misc': Report_Misc, 'Report_Echo': Report_Echo}