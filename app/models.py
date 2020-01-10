from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import app, db, login
from flask_login import UserMixin
from time import time
import jwt

#called to load a user given the ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    """How the class represents itself"""
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Report_CT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(24))
    docSerialNum = db.Column(db.String(20))
    patient = db.Column(db.String(24))
    species = db.Column(db.String(6))
    owner = db.Column(db.String(24))
    CT_Image_Date = db.Column(db.String(12))
    CT_NumImages = db.Column(db.Integer)
    CTView = db.Column(db.String(24))
    CT_Findings = db.Column(db.String(360))
    CT_Conclusions = db.Column(db.String(360))
    Clinic_Phone = db.Column(db.String(20))
    date = db.Column(db.String(12))
    clinicSerialNum = db.Column(db.Integer())
    clinic = db.Column(db.String(24))
    mvr4seasons = db.Column(db.String(24))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<CT for {}>'.format(self.patient)


class Report_Radiographic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(24))
    docSerialNum = db.Column(db.String(20))
    patient = db.Column(db.String(24))
    species = db.Column(db.String(6))
    owner = db.Column(db.String(24))
    Rad_Image_Date = db.Column(db.String(12))
    Rad_NumImages = db.Column(db.Integer)
    RadView = db.Column(db.String(24))
    Rad_Findings = db.Column(db.String(360))
    Rad_Conclusions = db.Column(db.String(360))
    Clinic_Phone = db.Column(db.String(20))
    date = db.Column(db.String(12))
    clinicSerialNum = db.Column(db.Integer())
    clinic = db.Column(db.String(24))
    mvr4seasons = db.Column(db.String(24))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Radiograph for {}>'.format(self.patient)


"""Ultrasound Database Class"""
class Report_US (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    docSerialNum = db.Column(db.String(20))
    patient = db.Column(db.String(24))
    owner = db.Column(db.String(24))
    species = db.Column(db.String(6))
    breed = db.Column(db.String(24))
    sexPatient = db.Column(db.String(2))
    agePatient = db.Column(db.String(24))
    clinicalHistory = db.Column(db.String(360))
    SF_Liver = db.Column(db.String(12))
    SF_Spleen = db.Column(db.String(12))
    SF_Stomach = db.Column(db.String(12))
    SF_Pancreas = db.Column(db.String(12))
    SF_Intestines = db.Column(db.String(12))
    SF_Adrenals = db.Column(db.String(12))
    SF_LKidney = db.Column(db.String(12))
    SF_RKidney = db.Column(db.String(12))
    SF_Bladder = db.Column(db.String(12))
    SF_Sublum = db.Column(db.String(12))
    SF_Prostate = db.Column(db.String(12))
    SF_Uterus = db.Column(db.String(12))
    Conclusions_ALL = db.Column(db.String(360))
    FINDAS_ALL = db.Column(db.String(360))
    date = db.Column(db.String(12))
    clinicSerialNum = db.Column(db.Integer())
    clinicName = db.Column(db.String(24))
    doctor = db.Column(db.String(24))
    mvr4seasons = db.Column(db.String(24))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Ultrasound for {}>'.format(self.patient)

"""Misc. Database Class"""
class Report_Misc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(24))
    docSerialNum = db.Column(db.String(20))
    clinicSerialNum = db.Column(db.Integer())
    clinicName = db.Column(db.String(24))
    mvr4seasons = db.Column(db.String(24))
    patient = db.Column(db.String(24))
    owner = db.Column(db.String(24))
    service = db.Column(db.String(24))
    SvcTotal = db.Column(db.Numeric)
    Misc_Service_Description = db.Column(db.String(300))
    date = db.Column(db.String(12))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Misc Report for {}>'.format(self.patient)

"""Echocardiography Database Class"""
class Report_Echo(db.Model):
    """Basic Fields"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12))
    doctor = db.Column(db.String(24))
    docSerialNum = db.Column(db.String(20))
    clinicSerialNum = db.Column(db.Integer())
    clinicName = db.Column(db.String(24))
    patient = db.Column(db.String(24))
    breed = db.Column(db.String(24))
    owner = db.Column(db.String(24))
    sexPatient = db.Column(db.String(2))
    agePatient = db.Column(db.String(24))
    weightPatient = db.Column(db.Float)
    clinicalHistory = db.Column(db.String(360))
    mvr4seasons = db.Column(db.String(24))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    """M-Mode Special Fields"""
    #LV Wall D
    LVFW_Distolic_Thickness = db.Column(db.Float)
    lower_range_LV_wall_D = db.Column(db.Float)
    upper_range_LV_wall_D = db.Column(db.Float)
    LVFW_DT_result = db.Column(db.String(5))
    #LV Wall S
    LVFW_Systolic_Thickness = db.Column(db.Float)
    lower_range_LV_wall_S = db.Column(db.Float)
    upper_range_LV_wall_S = db.Column(db.Float)
    LVFW_ST_result = db.Column(db.String(5))
    #LV Chamber D
    Left_Vent_Diastolic = db.Column(db.Float)
    lower_range_LV_Chamber_D = db.Column(db.Float)
    upper_range_LV_Chamber_D = db.Column(db.Float)
    LV_DD_result = db.Column(db.String(5))
    #LV Chamber S
    Left_Vent_Systolic = db.Column(db.Float)
    lower_range_LV_Chamber_S = db.Column(db.Float)
    upper_range_LV_Chamber_S = db.Column(db.Float)
    LV_SD_result = db.Column(db.String(5))
    #Fractional Shortening
    Shortening_Fraction = db.Column(db.Float)
    lower_range_fractional_shortening = db.Column(db.Float)
    upper_range_fractional_shortening = db.Column(db.Float)
    SF_result = db.Column(db.String(5))
    #Septum D
    IVS_Diastolic_Thickness = db.Column(db.Float)
    lower_range_septum_d = db.Column(db.Float)
    upper_range_septum_d = db.Column(db.Float)
    IVS_DT_result = db.Column(db.String(5))
    #Septum S
    IVS_Systolic_Thickness = db.Column(db.Float)
    lower_range_septum_s = db.Column(db.Float)
    upper_range_septum_s = db.Column(db.Float)
    IVS_ST_result = db.Column(db.String(5))
    #Aorta
    Aortic_Root = db.Column(db.Float)
    lower_range_aorta = db.Column(db.Float)
    upper_range_aorta = db.Column(db.Float)
    AR_result = db.Column(db.String(5))
    #Left Atrium
    Left_Atrium = db.Column(db.Float)
    lower_range_left_atrium = db.Column(db.Float)
    upper_range_left_atrium = db.Column(db.Float)
    LA_result = db.Column(db.String(5))
    #LA / AO
    Left_Atrium_over_AO = db.Column(db.Float)
    lower_range_la_over_ao = db.Column(db.Float)
    upper_range_la_over_ao = db.Column(db.Float)
    la_over_ao_result = db.Column(db.String(5))
    #EPSS
    EPSS = db.Column(db.Float)
    upper_range_epss = db.Column(db.Float)
    epss_result = db.Column(db.String(5))
    """Other Fields"""
    mMode_comments = db.Column(db.String(360))
    echo_doppler_findings = db.Column(db.String(450))
    Echo_B_mode_findings = db.Column(db.String(450))
    Echo_Conclusions = db.Column(db.String(450))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Echocardiographic Report for {}>'.format(self.patient)

"""Clinic Database Class"""
class Clinic(db.Model):
    clinicSerialNum = db.Column(db.String(64), primary_key=True)
    company = db.Column(db.String(64), unique=True)
    nickname = db.Column(db.String(64), unique=True)
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(10))
    zip = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(64))
    note = db.Column(db.String(140))
    doctors = db.relationship('Doctor', backref='clinic', lazy='dynamic')

    def __repr__(self):
        return '<Clinic {}>'.format(self.company)

"""Doctor Database Class"""
class Doctor(db.Model):
    doctorSerialNum = db.Column(db.String(64), primary_key=True)
    first = db.Column(db.String(24))
    middle = db.Column(db.String(3))
    last = db.Column(db.String(24))
    cell = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(64))
    note = db.Column(db.String(140))
    salutation = db.Column(db.String(4))
    clinicName = db.Column(db.String(20))
    clinicSerialNum = db.Column(db.String(64), db.ForeignKey('clinic.clinicSerialNum'))

    def __repr__(self):
        return '<Doctor {}>'.format(self.last)

"""Ultrasound Database Class"""
class MiscService(db.Model):
    serviceID = db.Column(db.String(20), primary_key=True)
    serviceType = db.Column(db.String(20))
    serviceAbbr = db.Column(db.String(10))
    reportType = db.Column(db.String(5))
    description = db.Column(db.String(144))
    servicePrice = db.Column(db.Numeric(6, 2))

    def __repr__(self):
        return '<Service {}>'.format(self.serviceType)