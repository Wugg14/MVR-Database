//Invoice Form Page
class InvoiceForm {

    constructor() {
        this.slot1 = document.getElementById('slot-1');
        this.slot2 = document.getElementById('slot-2');
        this.slot3 = document.getElementById('slot-3');
        this.service1 = document.getElementById('service1');
        this.service2 = document.getElementById('service2');
        this.service3 = document.getElementById('service3');
        // this.service4 = document.getElementById('service4');
        // this.service5 = document.getElementById('service5');
        // this.service6 = document.getElementById('service6');
        // this.service7 = document.getElementById('service7');
        // this.service8 = document.getElementById('service8');
        // this.service9 = document.getElementById('service9');
        // this.service10 = document.getElementById('service10');
        this.svcTotal = document.getElementById('priceTotal');
        this.events();
    }

     // Events
    events() {
        this.service1.addEventListener('change', function(){Invoice.updatePrice(Invoice.service1)});
        this.service2.addEventListener('change', function(){Invoice.updatePrice(Invoice.service2)});
        this.service3.addEventListener('change', function(){Invoice.updatePrice(Invoice.service3)});
        // this.service4.addEventListener('change', function(){Invoice.updatePrice(Invoice.service4)});
        // this.service5.addEventListener('change', function(){Invoice.updatePrice(Invoice.service5)});
        // this.service6.addEventListener('change', function(){Invoice.updatePrice(Invoice.service6)});
        // this.service7.addEventListener('change', function(){Invoice.updatePrice(Invoice.service7)});
        // this.service8.addEventListener('change', function(){Invoice.updatePrice(Invoice.service8)});
        // this.service9.addEventListener('change', function(){Invoice.updatePrice(Invoice.service9)});
        // this.service10.addEventListener('change', function(){Invoice.updatePrice(Invoice.service10)});

    }

    //Methods
    dispatcher(item){
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

        //if the price is in the report, not dictated by services table
        if(item.dataset.reportprice){
            let priceSlot = slot.querySelector('.reportPrice');
            let priceField = priceSlot.querySelector('input');
            priceField.value = item.dataset.reportprice;
        }

        slot.classList.add('filled');
    }

    updatePrice(row) {
        //Go find the next input in the parent elements sibling
        let priceInput = row.parentElement.nextElementSibling.querySelector('input');
        //Get the price from the stored value and split it from the name
        let price = row.value;
        price = price.split("__");
        price = price[1];
        //update price input
        priceInput.value = price;
        //update price total with helper method
        this.updateTotal()
    }

    updateTotal(){
        let total = 0;
        //Find all slots who have been filled with reports
        let filledSlots = document.getElementsByClassName('filled');
        //Iterate through HTMLCollection and extract the input value
        for(let item of filledSlots){
            let z = item.querySelector('.reportPrice').querySelector('input').value
            total += Number(z);
        }
        //Update the service total
        this.svcTotal.value = total;
    }

}

let Invoice = new InvoiceForm();
Invoice.svcTotal.value = 0;
