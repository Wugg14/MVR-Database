class EchocardiographForm {

    constructor() {
        // Work on this method after constructors
        this.prepareForm();
        //LV Wall D
        this.LVFW_Distolic_Thickness = document.getElementById('LVFW_Distolic_Thickness');
        this.lower_range_LV_wall_D = document.getElementById('lower_range_LV_wall_D');
        this.upper_range_LV_wall_D = document.getElementById('upper_range_LV_wall_D');
        this.LVFW_DT_result = document.getElementById('LVFW_DT_result');
        //LV Wall S
        this.LVFW_Systolic_Thickness = document.getElementById('LVFW_Systolic_Thickness');
        this.lower_range_LV_wall_S = document.getElementById('lower_range_LV_wall_S');
        this.upper_range_LV_wall_S = document.getElementById('upper_range_LV_wall_S');
        this.LVFW_ST_result = document.getElementById('LVFW_ST_result');
        //LV Chamber D
        this.Left_Vent_Diastolic = document.getElementById('Left_Vent_Diastolic');
        this.lower_range_LV_Chamber_D = document.getElementById('lower_range_LV_Chamber_D');
        this.upper_range_LV_Chamber_D = document.getElementById('upper_range_LV_Chamber_D');
        this.LV_DD_result = document.getElementById('LV_DD_result');
        //LV Chamber S
        this.Left_Vent_Systolic = document.getElementById('Left_Vent_Systolic');
        this.lower_range_LV_Chamber_S = document.getElementById('lower_range_LV_Chamber_S');
        this.upper_range_LV_Chamber_S = document.getElementById('upper_range_LV_Chamber_S');
        this.LV_SD_result = document.getElementById('LV_SD_result');
        //Fractional Shortening
        this.Shortening_Fraction = document.getElementById('Shortening_Fraction');
        this.lower_range_fractional_shortening = document.getElementById('lower_range_fractional_shortening');
        this.upper_range_fractional_shortening = document.getElementById('upper_range_fractional_shortening');
        this.SF_result = document.getElementById('SF_result');
        //Septum D
        this.IVS_Diastolic_Thickness = document.getElementById('IVS_Diastolic_Thickness');
        this.lower_range_septum_d = document.getElementById('lower_range_septum_d');
        this.upper_range_septum_d = document.getElementById('upper_range_septum_d');
        this.IVS_DT_result = document.getElementById('IVS_DT_result');
        //Septum S
        this.IVS_Systolic_Thickness = document.getElementById('IVS_Systolic_Thickness');
        this.lower_range_septum_s = document.getElementById('lower_range_septum_s');
        this.upper_range_septum_s = document.getElementById('upper_range_septum_s');
        this.IVS_ST_result = document.getElementById('IVS_ST_result');
        //Aorta
        this.Aortic_Root = document.getElementById('Aortic_Root');
        this.lower_range_aorta = document.getElementById('lower_range_aorta');
        this.upper_range_aorta = document.getElementById('upper_range_aorta');
        this.AR_result = document.getElementById('AR_result');
        //Left Atrium
        this.Left_Atrium = document.getElementById('Left_Atrium');
        this.lower_range_left_atrium = document.getElementById('lower_range_left_atrium');
        this.upper_range_left_atrium = document.getElementById('upper_range_left_atrium');
        this.LA_result = document.getElementById('LA_result');
        //LA/AO
        this.Left_Atrium_over_AO = document.getElementById('Left_Atrium_over_AO');
        this.lower_range_la_over_ao = document.getElementById('lower_range_la_over_ao');
        this.upper_range_la_over_ao = document.getElementById('upper_range_la_over_ao');
        this.la_over_ao_result = document.getElementById('la_over_ao_result');
        //EPSS
        this.EPSS = document.getElementById('EPSS');
        this.upper_range_epss = document.getElementById('upper_range_la_over_ao');
        this.epss_result = document.getElementById('epss_result');
        //Submit Button
        this.save = document.getElementById('submit');

    }
}

var echoForm= new EchocardiographForm();