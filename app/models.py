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

"""Ultrasound Database Class"""
class Report_US (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _KF_Doctor = db.Column(db.String(140))
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
    MVI_SIG_Doctor = db.Column(db.String(12))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    clinicSerialNum = db.Column(db.Integer())
    clinicName = db.Column(db.String(24))
    doctor = db.Column(db.String(24))

    def __repr__(self):
        return '<Ultrasound {}>'.format(self.id)




