from app import db
from app.models import Invoice, Invoice_Item, Clinic, Doctor, MiscService, Report_US, Report_Radiographic, Report_CT, Report_Misc

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

def make_additional_data():
    report1 = Report_US(doctor='test doc 1', docSerialNum='789', clinicName='test clinic 2', clinicSerialNum='456', patient='test patient 1', owner='test owner 1', species='Dog', breed='Shiba', sexPatient='Male', agePatient='12', clinicalHistory='this is a clinical history test', SF_Liver='test value', SF_Spleen='test value', SF_Stomach='test value', SF_Pancreas='test value', SF_Intestines='test value', SF_Adrenals='test value', SF_LKidney='test value', SF_RKidney='test value', SF_Bladder='test value', SF_Sublum='test value', SF_Prostate='test value', SF_Uterus='test value', Conclusions_ALL='test conclusion', FINDAS_ALL='test findings', date='010120', mvr4seasons='4seasons')
    db.session.add(report1)
    report2 = Report_Radiographic(date='010120', doctor='test doctor 2', docSerialNum='1011', clinic='test clinic 2', clinicSerialNum='456', patient='test patient 2', species='cat', owner='test owner 2', Rad_Image_Date='120119', Rad_NumImages='3', RadView='test view', Rad_Findings='these are the rad findings.', Rad_Conclusions='test rad conclusions', Clinic_Phone='9706919047', mvr4seasons='mvr')
    db.session.add(report2)
    report3 = Report_CT(doctor='test doctor 2', docSerialNum='1011', clinic='test Clinic 1', clinicSerialNum='123', patient='test patient', species='dog', owner='test owner', CT_Image_Date='111111', CT_NumImages=12, CTView='view 1', CT_Findings='test CT findings', CT_Conclusions='test ct conclusions', Clinic_Phone='9701287898', date='010120', mvr4seasons='4seasons')
    db.session.add(report3)
    report4 = Report_Misc(doctor='test doc 1', docSerialNum='789', clinicName='test clinic 2', clinicSerialNum='456', mvr4seasons='mvr', patient='test patient', owner='test owner', service='Type 1', SvcTotal=100, Misc_Service_Description='this is a misc service description', date='010120')
    db.session.add(report4)
    db.session.commit()

def makeInvoice():
    test = Invoice(invoiceID='111', date='2/21/20', mvr4seasons= 'mvr', clinic= 'test clinic 2', clinicSerialNum='456', doctor='Doctor2', docSerialNum='789', svcTotal= 1200)
    db.session.add(test)
    db.session.commit()

def addItem():
    test1 = Invoice_Item(invoiceID='111', serviceType='Echocardiography', reportID='1', patient='Pickles', price=1200)
    db.session.add(test1)
    db.session.commit()

def addExistingServices():
    ct = MiscService(serviceID='1', serviceType='CT Scan', serviceAbbr='ct', reportType='Report_CT', description='CT Scans', servicePrice=800)
    db.session.add(ct)
    radio = MiscService(serviceID='2', serviceType='Radiographic Interpretation', serviceAbbr='radio', reportType='Report_Radiographic', description='CT Scans', servicePrice=800)