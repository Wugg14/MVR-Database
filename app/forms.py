from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    """When you use a validate_<field_name>() structure for a function WTForms
    takes these as custom validators and invokes them in addition to stock validators"""
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class UltrasoundForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    patient = StringField('Patient:', validators=[DataRequired()])
    breed = StringField('Breed:', validators=[DataRequired()])
    doctor = StringField('Doctor:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    sex = StringField('Sex:', validators=[DataRequired()])
    practice = StringField('Practice:', validators=[DataRequired()])
    species = StringField('Species:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    clinicalHistory = TextAreaField('Clinical History:', validators=[DataRequired()])
    liver = SelectField('Liver/Gall bl:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below')])
    spleen = SelectField('Spleen:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below')])
    stomach = SelectField('Stomach:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below')])
    pancreas = SelectField('Pancr. area:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below')])
    intestines = SelectField('Intestines:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    adrenals = SelectField('Adrenals:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    lKidney = SelectField('Lt. Kidney', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    rKidney = SelectField('Rt. Kidney', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    bladder = SelectField('Bladder:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    sublum = SelectField('Sublum. area:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    prostate = SelectField('Prostate:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    uterus = SelectField('Uterus/Ov:', validators=[DataRequired()], choices=[('n', 'Normal'),('a', 'Abnormal'),('sb', 'See Below'), ('na', 'N.A.')])
    conclusions = TextAreaField('Conclusions:', validators=[DataRequired()])
    findings = TextAreaField('Impressions and Conclusions:', validators=[DataRequired()])
    submit = SubmitField('Save')

class radiographicInterpretationForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    patient = StringField('Patient:', validators=[DataRequired()])
    species = StringField('Species:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    doctor = StringField('Doctor:', validators=[DataRequired()])
    Rad_Image_Date = StringField('Date:', validators=[DataRequired()])
    practice = StringField('Practice:', validators=[DataRequired()])
    Rad_NumImages = IntegerField('No. of Images:', validators=[DataRequired()])
    phone = IntegerField('Phone:', validators=[DataRequired()])
    views = StringField('Views:', validators=[DataRequired()])
    Rad_Findings = TextAreaField('Findings:', validators=[DataRequired()])
    Rad_Conclusions = TextAreaField('Impressions and Conclusions:', validators=[DataRequired()])
    submit = SubmitField('Save')



