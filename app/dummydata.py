from app import db
from app.models import Clinic, Doctor, MiscService

def make_data():
    clinic1 = Clinic(clinicSerialNum='123', company='test Clinic 1', nickname='Nickname 1', street='Main St', city='Example City', state='Example State', zip='00000', phone='100-800-9320', email='test1@email.com', note='this is a note')
    clinic2 = Clinic(clinicSerialNum='456', company='test Clinic 2', nickname='Nickname 2', street='Main St 2', city='Example City 2', state='Example State 2', zip='22222', phone='200-800-9320', email='test2@email.com', note='this is a note')
    db.session.add(clinic1)
    db.session.add(clinic2)
    doctor1 = Doctor(doctorSerialNum='789', first='Test', middle='M', last='Doctor1', cell='900-600-4000', phone='900-600-4000', email='test1@email.com', note='this is a doc note', salutation='salutation', clinicName='Clinic 1', clinicSerialNum='123')
    doctor2 = Doctor(doctorSerialNum='1011', first='Test2', middle='M', last='Doctor2', cell='200-600-4000', phone='900-600-4000', email='test2@email.com', note='this is a doc note 2', salutation='salutation 2', clinicName='Clinic 2', clinicSerialNum='456')
    db.session.add(doctor1)
    db.session.add(doctor2)
    service1 = MiscService(serviceID='1213', serviceType='Type 1', serviceAbbr='Abbr 1', reportType='reportType1', description='description 1', servicePrice=100)
    service2 = MiscService(serviceID='1415', serviceType='Type 2', serviceAbbr='Abbr 2', reportType='reportType2', description='description 2', servicePrice=200)
    db.session.add(service1)
    db.session.add(service2)
    db.session.commit()


