from flask import render_template, redirect, url_for, flash
from app import db
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm, InvoiceForm, UltrasoundForm, radiographicInterpretationForm, ctInterpretationForm, newClinicForm, newDoctor, miscService, newService, EchocardiographForm
from app.models import User, Invoice, Invoice_Item, Clinic, Doctor, Report_US, Report_Radiographic, Report_CT, MiscService, Report_Misc, Report_Echo

def doctorEdit(entryID):
    form = newDoctor()
    doctorEntry = Doctor.query.filter(Doctor.doctorSerialNum == entryID).first()

    if form.validate_on_submit():
        clinicData = form.clinic.data
        # split serial from name by underscore seperator
        clinicData = clinicData.split('__')

        # update from the form
        doctorEntry.clinicName = clinicData[0]
        doctorEntry.clinicSerialNum = clinicData[1]
        doctorEntry.first = form.first.data
        doctorEntry.middle = form.middle.data
        doctorEntry.last = form.last.data
        doctorEntry.phone = form.phone.data
        doctorEntry.email = form.email.data
        doctorEntry.note = form.note.data

        db.session.commit()
        flash('Updated Doctor')
        return redirect(url_for('doctorTable'))

    return render_template('doctorForm.html', title='Edit Doctor', entry=doctorEntry, form=form)

def clinicEdit(entryID):
    form = newClinicForm()
    clinicEntry = Clinic.query.filter(Clinic.clinicSerialNum == entryID).first()

    if form.validate_on_submit():
        clinicEntry.company = form.company.data
        clinicEntry.nickname = form.nickname.data
        clinicEntry.street = form.street.data
        clinicEntry.city = form.city.data
        clinicEntry.state = form.state.data
        clinicEntry.zip = int(form.zip.data)
        clinicEntry.phone = form.phone.data
        clinicEntry.email = form.email.data
        clinicEntry.note = form.notes.data

        db.session.commit()
        flash('Updated Clinic')
        return redirect(url_for('clinicTable'))

    return render_template('clinicForm.html', title='Edit Clinic', entry=clinicEntry, form=form)



def echocardiographEdit(entryID):
    form = EchocardiographForm()
    formEntry = Report_Echo.query.filter(Report_Echo.id == entryID)

    if form.validate_on_submit():
        clinicData = form.practice.data
        clinicData = clinicData.split('__')
        doctorData = form.doctor.data
        doctorData = doctorData.split('__')

        formEntry.date = form.date.data
        formEntry.doctor = doctorData[0]
        formEntry.docSerialNum = doctorData[1]
        formEntry.clinicName = clinicData[0]
        formEntry.clinicSerialNum = clinicData[1]
        formEntry.mvr4seasons = form.mvr4seasons.data
        formEntry.patient = form.patient.data
        formEntry.species = form.species.data
        formEntry.breed = form.breed.data
        formEntry.owner = form.owner.data
        formEntry.sexPatient = form.sex.data
        formEntry.agePatient = form.age.data,
        formEntry.weightPatient = form.weight.data
        formEntry.clinicalHistory = form.clinicalHistory.data
        formEntry.LVFW_Distolic_Thickness = form.LVFW_Distolic_Thickness.data
        formEntry.lower_range_LV_wall_D = form.lower_range_LV_wall_D.data
        formEntry.upper_range_LV_wall_D = form.upper_range_LV_wall_D.data
        formEntry.LVFW_DT_result = form.LVFW_DT_result.data
        formEntry.LVFW_Systolic_Thickness = form.LVFW_Systolic_Thickness.data
        formEntry.lower_range_LV_wall_S = form.lower_range_LV_wall_S.data
        formEntry.upper_range_LV_wall_S = form.upper_range_LV_wall_S.data
        formEntry.LVFW_ST_result = form.LVFW_ST_result.data
        formEntry.Left_Vent_Diastolic = form.Left_Vent_Diastolic.data
        formEntry.lower_range_LV_Chamber_D = form.lower_range_LV_Chamber_D.data
        formEntry.upper_range_LV_Chamber_D = form.upper_range_LV_Chamber_D.data
        formEntry.LV_DD_result = form.LV_DD_result.data
        formEntry.Left_Vent_Systolic = form.Left_Vent_Systolic.data
        formEntry.lower_range_LV_Chamber_S = form.lower_range_LV_Chamber_S.data
        formEntry.upper_range_LV_Chamber_S = form.upper_range_LV_Chamber_S.data
        formEntry.LV_SD_result = form.LV_SD_result.data
        formEntry.Shortening_Fraction = form.Shortening_Fraction
        formEntry.lower_range_fractional_shortening = form.lower_range_fractional_shortening.data
        formEntry.upper_range_fractional_shortening = form.upper_range_fractional_shortening.data
        formEntry.SF_result = form.SF_result.data
        formEntry.IVS_Diastolic_Thickness = form.IVS_Diastolic_Thickness.data
        formEntry.lower_range_septum_d = form.lower_range_septum_d.data
        formEntry.upper_range_septum_d = form.upper_range_septum_d.data
        formEntry.IVS_DT_result = form.IVS_DT_result.data
        formEntry.IVS_Systolic_Thickness = form.IVS_Systolic_Thi
        formEntry.lower_range_septum_s = form.lower_range_septum_s.data
        formEntry.upper_range_septum_s = form.upper_range_septum_s.data
        formEntry.IVS_ST_result = form.IVS_ST_result.data
        formEntry.Aortic_Root = form.Aortic_Root.data
        formEntry.lower_range_aorta = form.lower_range_aorta.data
        formEntry.upper_range_aorta = form.upper_range_aorta.data
        formEntry.AR_result = form.AR_result.data
        formEntry.Left_Atrium = form.Left_Atrium.data
        formEntry.lower_range_left_atrium = form.lower_range_left_atrium.data
        formEntry.upper_range_left_atrium = form.upper_range_left_atrium.data
        formEntry.LA_result = form.LA_result.data
        formEntry.Left_Atrium_over_AO = form.Left_Atrium_over_AO.data
        formEntry.lower_range_la_over_ao = form.lower_range_la_over_ao.data
        formEntry.upper_range_la_over_ao = form.upper_range_la_over_ao.data
        formEntry.la_over_ao_result = form.la_over_ao_result.data
        formEntry.EPSS = form.EPSS.data
        formEntry.upper_range_epss = form.upper_range_epss.data
        formEntry.epss_result = form.epss_result.data
        formEntry.mMode_comments = form.m_mode_comments.data
        formEntry.echo_doppler_findings = form.echo_doppler_findings.data
        formEntry.Echo_B_mode_findings = form.Echo_B_mode_findings.data
        formEntry.Echo_Conclusions = form.Echo_Conclusions.data

        db.session.commit()
        flash('Updated Cardiographic Report')
        return redirect(url_for('echoTable'))

    return render_template('echocardiograph.html', title='Edit Cardiographic Report', entry=formEntry, form=form)
