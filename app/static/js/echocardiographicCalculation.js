class EchocardiographForm {

    constructor() {
        this.weightLbs = document.getElementById('weight');
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
        this.calcButton = document.getElementById('calculate');
        //this.hideSaveButton();
        this.events();
    }

    // Events
    events() {
        this.calcButton.addEventListener('click', this.calculateDispatcher.bind(this))
    }

    //Methods
    hideSaveButton(){
        this.save.style.display = 'none';
        return true;
    }

    showSaveButton(){
        this.save.style.display = 'block';
        return true;
    }

    testMethods(){
        console.log('test Method')
    }

    calculateDispatcher(){
        this.septumDCalc();
        this.lvChamberD();
        this.lvWallD()
        this.septumS()
    }




    neededWeights(requestedVal){
        let lbs = this.weightLbs.value;
        let kg = lbs/2.2046;
        let gram = kg * 1000;

        if (requestedVal == 'lbs') {
            return lbs;
        }

        if (requestedVal == 'kgs') {
            return kg;
        }

        if (requestedVal == 'grams') {
            return gram;
        }
    }


    calculateBSA(){
        let grams = this.neededWeights('grams');
        let firstCalc = grams**(2/3);
        let secondCalc = 10.1 * firstCalc;
        let thirdCalc = secondCalc / (10**4);
        //return rounded to second decimal point
        return thirdCalc.toFixed(2);
    }

    increaseOrDecrease (val, upper, lower) {
        if (val > upper) {
            return 'Incr'
        }

        if (val < lower) {
            return 'Decr'
        } else {
            return 'Nor'
        }
    }

    septumDCalc() {
        let BSA = this.calculateBSA();
        let Y = 5.27 + (5.6*BSA);
        let SY = (1.762) * ((0.016 + (((BSA - 0.75)**2) / 5.054))**0.5);
        let lower = Y - (1.999 * SY);
        let upper = Y + (1.999 * SY);
        this.lower_range_septum_d.value = lower;
        this.upper_range_septum_d.value = upper;
        let enteredVal = this.IVS_Diastolic_Thickness.value;
        this.IVS_DT_result.value = this.increaseOrDecrease(enteredVal, upper, lower);
        return(true);
    }

    lvChamberD(){
        let KG =  this.neededWeights('kgs');
        let Y = 5.66 + 9.416 * Math.log(KG);
        console.log('y = ' + Y)
        let SY = 2*(2.9*(Math.sqrt(0.015+(KG-27.4)**2/25947.2)));
        console.log('sy = '+ SY)
        let lower = Y - SY;
        let upper = Y + SY;
        this.lower_range_LV_Chamber_D.value = lower;
        this.upper_range_LV_Chamber_D.value = upper;
        let enteredVal = this.Left_Vent_Diastolic.value;
        this.LV_DD_result.value = this.increaseOrDecrease(enteredVal, upper, lower);
        return(true);
    }

    lvWallD(){
        let BSA = this.calculateBSA();
        let Y = 4.18 + 4.61 * BSA;
        let SY = (1.48) * ((0.016 + (((BSA  - 0.74)**2) / 5.147))**0.5);
        let lower = Y - (1.999 * SY);
        let upper = Y + (1.999 * SY);
        this.lower_range_LV_wall_D.value = lower;
        this.upper_range_LV_wall_D.value = upper;
        let enteredVal = this.LVFW_Distolic_Thickness.value;
        this.LVFW_DT_result.value = this.increaseOrDecrease(enteredVal, upper, lower);
        return(true);
    }

    septumS(){
        let BSA = this.calculateBSA();
        let Y = 7.53 + 8.75 * BSA;
        let SY = (1.963) * ((0.016 + (((BSA - 0.75)**2) / 5.054))**0.5);
        let lower = Y - (1.999 * SY);
        let upper = Y + (1.999 * SY);
        this.lower_range_septum_s.value = lower;
        this.upper_range_septum_s.value = upper;
        let enteredVal = this.IVS_Systolic_Thickness.value;
        this.IVS_ST_result.value = this.increaseOrDecrease(enteredVal, upper, lower);
        return(true);
    }

}


let echoForm = new EchocardiographForm();