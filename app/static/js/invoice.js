//Invoice Form Page
class InvoiceForm {

    constructor() {
        this.slot1 = document.getElementById('slot-1');
        this.slot2 = document.getElementById('slot-2');
        this.slot3 = document.getElementById('slot-3');
        this.service1 = document.getElementById('service1')

    }

     // Events
    events() {
        this.service1.addEventListener('change', this.updatePrice(this.service1))
    }

    //Methods
    dispatcher(item){
        let z = item.dataset.reportid;
        console.log(z);
        let slot = this.identifySlot();
        this.fillSlot(slot, item)
    }

    identifySlot(){
        if (!this.slot1.classList.contains('filled')) {
            return this.slot1
        }

        else if(!this.slot2.classList.contains('filled')) {
            return this.slot2
        }

        else if(!this.slot3.classList.contains('filled')) {
            return this.slot3
        }
    }

    fillSlot(slot, item){
        let idSlot = slot.querySelector('.reportID');
        let idField = idSlot.querySelector('input');
        idField.value = item.dataset.reportid;

        let patientSlot = slot.querySelector('.reportPatient');
        let patientField = patientSlot.querySelector('input');
        patientField.value = item.dataset.reportpatient;

        let doctorSlot = slot.querySelector('.reportDoctor');
        let doctorField = doctorSlot.querySelector('input');
        doctorField.value = item.dataset.reportdoctor;

        if(item.dataset.reportprice){
            let priceSlot = slot.querySelector('.reportPrice');
            let priceField = priceSlot.querySelector('input');
            priceField.value = item.dataset.reportprice;
        }

        slot.classList.add("filled");
    }

    updatePrice(row) {
        //update the correspoding price
    }


}

let Invoice = new InvoiceForm();