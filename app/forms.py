from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from app.getCurrentClinics import get_current_clinics
from app.getCurrentDoctors import get_current_doctors
from app.getCurrentServices import get_current_services

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

class newClinicForm (FlaskForm):
    company = StringField('Company:', validators=[DataRequired()])
    nickname = StringField('Nickname:', validators=[DataRequired()])
    street = StringField('Street:', validators=[DataRequired()])
    city = StringField('City:', validators=[DataRequired()])
    state = StringField('State:', validators=[DataRequired()])
    zip = IntegerField('Zip Code:', validators=[DataRequired()])
    phone = IntegerField('Phone:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    notes = StringField('Notes:')
    submit = SubmitField('Save')

class newDoctor (FlaskForm):
    clinic = SelectField('Company:', validators=[DataRequired()], choices=get_current_clinics())
    first = StringField('First Name:', validators=[DataRequired()])
    middle = StringField('Middle Initial:')
    last = StringField('Last Name:', validators=[DataRequired()])
    phone = IntegerField('Phone:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    note = StringField('Notes:', validators=[DataRequired()])
    submit = SubmitField('Save')

class EchocardiographForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
    doctor = SelectField('Doctor:', validators=[DataRequired()], choices=get_current_doctors())
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    patient = StringField('Patient:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    age = StringField('Age:')
    species = StringField('Species:', validators=[DataRequired()])
    breed = StringField('Breed:', validators=[DataRequired()])
    sex = StringField('Sex:', validators=[DataRequired()])
    weight = StringField('Weight (lbs):', validators=[DataRequired()])
    clinicalHistory = TextAreaField('Clinical History:', validators=[DataRequired()])
    # LV Wall-d
    LVFW_Distolic_Thickness = StringField('LVFW_Distolic_Thickness:', validators=[DataRequired()])
    lower_range_LV_wall_D = StringField('lower_range_LV_wall_D:')
    upper_range_LV_wall_D = StringField('upper_range_LV_wall_D:')
    LVFW_DT_result = StringField('LVFW_DT_result:')
    # LV Wall-s
    LVFW_Systolic_Thickness = StringField('LVFW_Systolic_Thickness:', validators=[DataRequired()])
    lower_range_LV_wall_S = StringField('lower_range_LV_wall_S:')
    upper_range_LV_wall_S = StringField('upper_range_LV_wall_S:')
    LVFW_ST_result = StringField('LVFW_ST_result:')
    # LV Chamber-d:
    Left_Vent_Diastolic = StringField('Left_Vent_Diastolic:', validators=[DataRequired()])
    lower_range_LV_Chamber_D = StringField('lower_range_LV_Chamber_D:')
    upper_range_LV_Chamber_D = StringField('upper_range_LV_Chamber_D:')
    LV_DD_result = StringField('LV_DD_result:')
    # LV Chamber-s:
    Left_Vent_Systolic = StringField('Left_Vent_Systolic:', validators=[DataRequired()])
    lower_range_LV_Chamber_S = StringField('lower_range_LV_Chamber_S:')
    upper_range_LV_Chamber_S = StringField('upper_range_LV_Chamber_S:')
    LV_SD_result = StringField('LV_SD_result:')
    # Fractional Shortening
    Shortening_Fraction = StringField('Shortening_Fraction:', validators=[DataRequired()])
    lower_range_fractional_shortening = StringField('lower_range_fractional_shortening:')
    upper_range_fractional_shortening = StringField('upper_range_fractional_shortening:')
    SF_result = StringField('SF_result:')
    # Septum-d
    IVS_Diastolic_Thickness = StringField('IVS_Diastolic_Thickness:', validators=[DataRequired()])
    lower_range_septum_d = StringField('lower_range_septum_d:')
    upper_range_septum_d = StringField('upper_range_septum_d:')
    IVS_DT_result = StringField('IVS_DT_result:')
    # Septum-s
    IVS_Systolic_Thickness = StringField('IVS_Systolic_Thickness:', validators=[DataRequired()])
    lower_range_septum_s = StringField('lower_range_septum_s:')
    upper_range_septum_s = StringField('upper_range_septum_s:')
    IVS_ST_result = StringField('IVS_ST_result:')
    # Aorta
    Aortic_Root = StringField('Aortic_Root:', validators=[DataRequired()])
    lower_range_aorta = StringField('lower_range_aorta:')
    upper_range_aorta = StringField('upper_range_aorta:')
    AR_result = StringField('AR_result:')
    # Left Atrium
    Left_Atrium = StringField('Left_Atrium:', validators=[DataRequired()])
    lower_range_left_atrium = StringField('lower_range_left_atrium:')
    upper_range_left_atrium = StringField('upper_range_left_atrium:')
    LA_result = StringField('LA_result:')
    # LA/AO
    Left_Atrium_over_AO = StringField('Left_Atrium_over_AO:', validators=[DataRequired()])
    lower_range_la_over_ao = StringField('lower_range_la_over_ao:')
    upper_range_la_over_ao = StringField('upper_range_la_over_ao:')
    la_over_ao_result = StringField('la_over_ao_result:')
    # EPSS has only 3 fields
    EPSS = StringField('EPSS:', validators=[DataRequired()])
    upper_range_epss = StringField('upper_range_epss:')
    epss_result = StringField('epss_result:')
    # Comments
    m_mode_comments = StringField('M-Mode Comments:')
    echo_doppler_findings = TextAreaField('Doppler:', validators=[DataRequired()])
    Echo_B_mode_findings = TextAreaField('B-Mode:', validators=[DataRequired()])
    Echo_Conclusions = TextAreaField('Impressions and Conclusions:', validators=[DataRequired()])
    submit = SubmitField('Save')

class UltrasoundForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    patient = StringField('Patient:', validators=[DataRequired()])
    breed = StringField('Breed:', validators=[DataRequired()])
    doctor = SelectField('Doctor:', validators=[DataRequired()], choices=get_current_doctors())
    owner = StringField('Owner:', validators=[DataRequired()])
    sex = StringField('Sex:', validators=[DataRequired()])
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    species = StringField('Species:', validators=[DataRequired()])
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
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
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
    patient = StringField('Patient:', validators=[DataRequired()])
    species = StringField('Species:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    doctor = SelectField('Doctor:', validators=[DataRequired()], choices=get_current_doctors())
    Rad_Image_Date = StringField('Image Date:', validators=[DataRequired()])
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    Rad_NumImages = IntegerField('No. of Images:', validators=[DataRequired()])
    phone = IntegerField('Phone:', validators=[DataRequired()])
    views = StringField('Views:', validators=[DataRequired()])
    Rad_Findings = TextAreaField('Findings:', validators=[DataRequired()])
    Rad_Conclusions = TextAreaField('Impressions and Conclusions:', validators=[DataRequired()])
    submit = SubmitField('Save')

class ctInterpretationForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
    patient = StringField('Patient:', validators=[DataRequired()])
    species = StringField('Species:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    doctor = SelectField('Doctor:', validators=[DataRequired()], choices=get_current_doctors())
    CT_Image_Date = StringField('Image Date:', validators=[DataRequired()])
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    CT_NumImages = IntegerField('No. of Images:', validators=[DataRequired()])
    phone = StringField('Phone:', validators=[DataRequired()])
    views = StringField('Views:', validators=[DataRequired()])
    CT_Findings = TextAreaField('Findings:', validators=[DataRequired()])
    CT_Conclusions = TextAreaField('Impressions and Conclusions:', validators=[DataRequired()])
    submit = SubmitField('Save')

class miscService (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
    doctor = SelectField('Doctor:', validators=[DataRequired()], choices=get_current_doctors())
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    patient = StringField('Patient:', validators=[DataRequired()])
    owner = StringField('Owner:', validators=[DataRequired()])
    service = SelectField('Service:', validators=[DataRequired()], choices=get_current_services())
    charge = StringField('Charge:', validators=[DataRequired()])
    description = StringField('Service Description:', validators=[DataRequired()])
    submit = SubmitField('Save')

class newService (FlaskForm):
    serviceType = StringField('Service Type:', validators=[DataRequired()])
    serviceAbbr = StringField('Service Abbreviation:', validators=[DataRequired()])
    ReportType = SelectField('Report Type:', validators=[DataRequired()], choices=[('US', 'Ultrasound'), ('Misc', 'Misc'), ('Rad', 'Radiographic'), ('CT', 'CT'), ('Echo', 'Echocardiograph')])
    description = StringField('Description:', validators=[DataRequired()])
    price = FloatField('Price:', validators=[DataRequired()])
    submit = SubmitField('Save')

class InvoiceForm (FlaskForm):
    date = StringField('Date:', validators=[DataRequired()])
    mvr4seasons = SelectField('MVR or 4 Seasons:', validators=[DataRequired()], choices=[('4seasons', '4 Seasons'), ('mvr', 'MVR')])
    doctor = StringField('Doctor:', validators=[DataRequired()])
    practice = SelectField('Practice:', validators=[DataRequired()], choices=get_current_clinics())
    #Invoice Slot 1
    patient1 = StringField('Patient:', validators=[DataRequired()])
    doctor1 = StringField('Doctor:', validators=[DataRequired()])
    service1 = SelectField('Service:', validators=[DataRequired()], choices=get_current_services())
    price1 = StringField('Price:', validators=[DataRequired()])
    reportID1 = StringField('ID:', validators=[DataRequired()])
    #Invoice Slot 2
    patient2 = StringField('Patient:', validators=[DataRequired()])
    doctor2 = StringField('Doctor:', validators=[DataRequired()])
    service2 = SelectField('Service:', validators=[DataRequired()], choices=get_current_services())
    price2 = StringField('Price:', validators=[DataRequired()])
    reportID2 = StringField('ID:', validators=[DataRequired()])
    # Invoice Slot 3
    patient3 = StringField('Patient:', validators=[DataRequired()])
    doctor3 = StringField('Doctor:', validators=[DataRequired()])
    service3 = SelectField('Service:', validators=[DataRequired()], choices=get_current_services())
    price3 = StringField('Price:', validators=[DataRequired()])
    reportID3 = StringField('ID:', validators=[DataRequired()])
    submit = SubmitField('Save')
