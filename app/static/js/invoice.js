//Invoice Form Page
class InvoiceForm {

    constructor() {
        this.buttons = document.getElementsByClassName('add-to-invoice');
    }

     // Events
    events() {

    }

    //Methods
    test(item){
        console.log(item)
       let z = item.dataset.reportid;
    }

}

let Invoice = new InvoiceForm();