from flask import render_template, request, redirect, url_for, flash
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm, UltrasoundForm, radiographicInterpretationForm, ctInterpretationForm, newClinicForm, newDoctor, miscService
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Clinic, Doctor, Report_US, Report_Radiographic
from app.email import send_password_reset_email
from app.randomStrings import randomStringDigits

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #For case in which user is already logged in, but navigates to login page
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/ultrasound', methods=['GET', 'POST'])
def ultrasound():
    form = UltrasoundForm()
    if form.validate_on_submit():
        clinicData = form.practice.data
        clinicData = clinicData.split('__')
        doctorData = form.doctor.data
        doctorData = doctorData.split('__')
        ultrasound = Report_US(doctor=doctorData[0], docSerialNum=doctorData[1], clinicName=clinicData[0], clinicSerialNum=clinicData[1], patient=form.patient.data, owner=form.owner.data, species=form.species.data, breed=form.breed.data, sexPatient=form.sex.data, agePatient=form.age.data, clinicalHistory=form.age.data, SF_Liver=form.liver.data, SF_Spleen=form.spleen.data, SF_Stomach=form.stomach.data, SF_Pancreas=form.pancreas.data, SF_Intestines=form.intestines.data, SF_Adrenals=form.adrenals.data, SF_LKidney=form.lKidney.data, SF_RKidney=form.rKidney.data, SF_Bladder=form.bladder.data, SF_Sublum=form.sublum.data, SF_Prostate=form.prostate.data, SF_Uterus=form.uterus.data, Conclusions_ALL=form.conclusions.data, FINDAS_ALL=form.findings.data, date=form.date.data, mvr4seasons=form.mvr4seasons.data)
        db.session.add(ultrasound)
        db.session.commit()
        flash('Added Ultrasound Report to database')
        return redirect(url_for('ultrasoundTable'))
    return render_template('ultrasound.html', title='Ultrasound Report', form=form)

@app.route('/radiograph', methods=['GET', 'POST'])
def radiograph():
    form = radiographicInterpretationForm()
    if form.validate_on_submit():
        clinicData = form.practice.data
        clinicData = clinicData.split('__')
        print(clinicData)
        doctorData = form.doctor.data
        doctorData = doctorData.split('__')
        print(clinicData)
        radiographReport = Report_Radiographic(doctor=doctorData[0], docSerialNum=doctorData[1], clinic=clinicData[0], clinicSerialNum=clinicData[1], patient=form.patient.data, species=form.species.data, owner=form.owner.data, Rad_Image_Date=form.Rad_Image_Date.data, Rad_NumImages=form.Rad_NumImages.data, RadView=form.views.data, Rad_Findings=form.Rad_Findings.data,Rad_Conclusions=form.Rad_Conclusions.data, Clinic_Phone=form.phone.data,mvr4seasons=form.mvr4seasons.data)
        db.session.add(radiographReport)
        db.session.commit()
        flash('Added report to database')
        return redirect(url_for('radiograph'))
    return render_template('radiograph.html', title='Ultrasound Report', form=form)

@app.route('/ct', methods=['GET', 'POST'])
def CT():
    form = ctInterpretationForm()
    return render_template('ct.html', title='CT Report', form=form)

@app.route('/misc', methods=['GET', 'POST'])
def misc():
    form = miscService()
    return render_template('miscService.html', title='Misc Service Report', form=form)


@app.route('/newclinic', methods=['GET', 'POST'])
def newClinic():
    form = newClinicForm()
    if form.validate_on_submit():
        clinic = Clinic(company=form.company.data, nickname=form.nickname.data, street=form.street.data, city=form.city.data, state=form.state.data, zip=form.zip.data, phone=form.phone.data, email=form.email.data, note=form.notes.data, clinicSerialNum=randomStringDigits(8))
        db.session.add(clinic)
        db.session.commit()
        flash('Added clinic to database')
        return redirect(url_for('newClinic'))
    return render_template('clinicForm.html', title='New Clinic', form=form)

@app.route('/newdoc', methods=['GET', 'POST'])
def newDoc():
    form = newDoctor()
    if form.validate_on_submit():
        clinicData = form.clinic.data
        #split serial from name by underscore seperator
        clinicData = clinicData.split('__')
        doctor = Doctor(clinicName=clinicData[0], clinicSerialNum=clinicData[1], first=form.first.data, middle=form.middle.data, last=form.last.data, phone=form.phone.data, email=form.email.data, note=form.note.data, doctorSerialNum=randomStringDigits(8))
        db.session.add(doctor)
        db.session.commit()
        flash('Added doctor to database')
        return redirect(url_for('newDoc'))

    return render_template('doctorForm.html', title='New Doctor', form=form)


@app.route('/clinictable', methods=['GET', 'POST'])
def clinicTable():
    clinics = Clinic.query.all()
    return render_template('/tables/clinicTable.html',  title='All Clinics', clinics=clinics)

@app.route('/doctortable', methods=['GET', 'POST'])
def doctorTable():
    doctors = Doctor.query.all()
    return render_template('/tables/doctorTable.html',  title='All Doctors', doctors=doctors)

@app.route('/ultrasoundtable', methods=['GET'])
def ultrasoundTable():
    ultrasounds = Report_US.query.all()
    return render_template('/tables/ultrasoundTable.html', title='All Ultrasounds', ultrasounds=ultrasounds)

@app.route('/radiographtable', methods=['GET'])
def radiographTable():
    radiographs = Report_Radiographic.query.all()
    return render_template('/tables/radiographTable.html', title='All Radiographic Reports', radiographs=radiographs)