from flask import render_template, redirect, url_for, flash
from app import db
from app.forms import InvoiceForm, UltrasoundForm, radiographicInterpretationForm, ctInterpretationForm, newClinicForm, newDoctor, miscService, newService, EchocardiographForm
from app.models import Invoice, Invoice_Item, Clinic, Doctor, Report_US, Report_Radiographic, Report_CT, MiscService, Report_Misc, Report_Echo
from app.structureSelectFields import structure_options

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
    formEntry = Report_Echo.query.filter(Report_Echo.id == entryID)
    structuredDoc = structure_options(formEntry.doctor, formEntry.docSerialNum)
    form = EchocardiographForm(doctor=structuredDoc)

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

def miscServiceEdit(entryID):
    formEntry = Report_Misc.query.filter(Report_Misc.id == entryID).first()
    structuredDoc = structure_options(formEntry.doctor, formEntry.docSerialNum)
    form = miscService(doctor=structuredDoc)


    if form.validate_on_submit():
        clinicData = form.practice.data
        clinicData = clinicData.split('__')
        doctorData = form.doctor.data
        doctorData = doctorData.split('__')
        serviceData = form.service.data
        serviceData = serviceData.split('__')

        formEntry.doctor = doctorData[0]
        formEntry.docSerialNum = doctorData[1]
        formEntry.clinicName = clinicData[0]
        formEntry.clinicSerialNum = clinicData[1]
        formEntry.mvr4seasons = form.mvr4seasons.data
        formEntry.patient = form.patient.data
        formEntry.owner = form.owner.data
        formEntry.service = serviceData[0]
        formEntry.SvcTotal = form.charge.data
        formEntry.Misc_Service_Description = form.description.data
        formEntry.date = form.date.data

        db.session.commit()
        flash('Updated Misc Report')

        return redirect(url_for('miscReportTable'))

    return render_template('miscService.html', title='Edit Misc Report', entry=formEntry, form=form)

def editService(entryID):
    formEntry = MiscService.query.filter(MiscService.serviceID == entryID).first()
    form = newService()

    if form.validate_on_submit():
        formEntry.serviceType = form.serviceType.data
        formEntry.serviceAbbr = form.serviceAbbr.data
        formEntry.reportType = form.ReportType.data
        formEntry.description = form.description.data
        formEntry.servicePrice = form.price.data

        db.session.commit()
        flash('Updated Service')

        return redirect(url_for('serviceTable'))

    return render_template('newService.html', title='Edit Service', entry=formEntry, form=form)

#radiograph
def editRadiograph(entryID):
    formEntry = Report_Radiographic.query.filter(Report_Radiographic.id == entryID).first()
    form = radiographicInterpretationForm()

    if form.validate_on_submit():
        formEntry.date = form.date.data
        formEntry.doctor = doctorData[0]
        formEntry.docSerialNum = doctorData[1]
        formEntry.clinic = clinicData[0]
        formEntry.clinicSerialNum = clinicData[1]
        formEntry.patient = form.patient.data
        formEntry.species = form.species.data
        formEntry.owner = form.owner.data
        formEntry.Rad_Image_Date = form.Rad_Image_Date.data
        formEntry.Rad_NumImages = form.Rad_NumImages.data
        formEntry.RadView = form.views.data
        formEntry.Rad_Findings = form.Rad_Findings.data
        formEntry.Rad_Conclusions = form.Rad_Conclusions.data
        formEntry.Clinic_Phone = form.phone.data
        formEntry.mvr4seasons = form.mvr4seasons.data

        db.session.commit()
        flash('Updated Radiographic Interpretation')
        return redirect(url_for('radiographTable'))

    return render_template('radiograph.html', title='Edit Radiographic Interpretation', entry=formEntry, form=form)

def editUltrasound(entryID):
    formEntry = Report_US.query.filter(Report_US.id == entryID).first()
    form = UltrasoundForm()

    if form.validate_on_submit():
        formEntry.doctor = doctorData[0]
        formEntry.docSerialNum = doctorData[1]
        formEntry.clinicName = clinicData[0]
        formEntry.clinicSerialNum = clinicData[1]
        formEntry.patient = form.patient.data
        formEntry.owner = form.owner.data
        formEntry.species = form.species.data
        formEntry.breed = form.breed.data
        formEntry.sexPatient = form.sex.data
        formEntry.agePatient = form.age.data
        formEntry.clinicalHistory = form.age.data
        formEntry.SF_Liver = form.liver.data
        formEntry.SF_Spleen = form.spleen.data
        formEntry.SF_Stomach = form.stomach.data
        formEntry.SF_Pancreas = form.pancreas.data
        formEntry.SF_Intestines = form.intestines.data
        formEntry.SF_Adrenals = form.adrenals.data
        formEntry.SF_LKidney = form.lKidney.data
        formEntry.SF_RKidney = form.rKidney.data
        formEntry.SF_Bladder = form.bladder.data
        formEntry.SF_Sublum = form.sublum.data
        formEntry.SF_Prostate = form.prostate.data
        formEntry.SF_Uterus = form.uterus.data
        formEntry.Conclusions_ALL = form.conclusions.data
        formEntry.FINDAS_ALL = form.findings.data
        formEntry.date = form.date.data
        formEntry.mvr4seasons = form.mvr4seasons.data

        db.session.commit()
        flash('Updated Ultrasound Report')

        return redirect(url_for('ultrasoundTable'))

    return render_template('ultrasound.html', title='Edit Ultrasound Report', entry=formEntry, form=form)

def editCT(entryID):
    formEntry = Report_CT.query.filter(Report_CT.id == entryID).first()
    form = ctInterpretationForm()

    if form.validate_on_submit():
        formEntry.doctor = doctorData[0]
        formEntry.docSerialNum = doctorData[1]
        formEntry.clinic = clinicData[0]
        formEntry.clinicSerialNum = clinicData[1]
        formEntry.patient = form.patient.data
        formEntry.species = form.species.data
        formEntry.owner = form.owner.data
        formEntry.CT_Image_Date = form.CT_Image_Date.data
        formEntry.CT_NumImages = form.CT_NumImages.data
        formEntry.CTView = form.views.data
        formEntry.CT_Findings = form.CT_Findings.data
        formEntry.CT_Conclusions = form.CT_Conclusions.data
        formEntry.Clinic_Phone = form.phone.data
        formEntry.date = form.date.data
        formEntry.mvr4seasons = form.mvr4seasons.data

        db.session.commit()
        flash('Updated CT Report')
        return redirect(url_for('ctTable'))

    return render_template('ct.html', title='Edit CT Report', entry=formEntry, form=form)







