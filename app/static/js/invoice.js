//Invoice Form Page
class InvoiceForm {

    constructor() {
        this.slot1 = document.getElementById('slot-1');
        this.slot2 = document.getElementById('slot-2');
        this.slot3 = document.getElementById('slot-3');
        this.service1 = document.getElementById('service1');
        this.service2 = document.getElementById('service2');
        this.service3 = document.getElementById('service3');

        this.events();
    }

     // Events
    events() {
        this.service1.addEventListener('change', function(){Invoice.updatePrice(Invoice.service1)})
        this.service2.addEventListener('change', function(){Invoice.updatePrice(Invoice.service2)})
        this.service3.addEventListener('change', function(){Invoice.updatePrice(Invoice.service3)})
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
        console.log('updatePrice')
        //Go find the next input in the parent elements sibling
        let priceInput = row.parentElement.nextElementSibling.querySelector('input');
        //Get the price from the stored value and split it from the name
        let price = row.value;
        price = price.split("__");
        price = price[1];
        //update price input
        priceInput.value = price;
    }


}

let Invoice = new InvoiceForm();