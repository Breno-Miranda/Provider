import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.scss']
})
export class NewComponent implements OnInit {
  [x: string]: any;

  constructor(
     private formBuilder: FormBuilder,
  ) {
  }


  requestForm: FormGroup;


  ngOnInit() {
    // Form
    const form = $('#example-form');
    form.children('div').steps({
      headerTag: 'h3',
      bodyTag: 'section',
      transitionEffect: 'slideLeft',
      onFinished(event, currentIndex) {
        window.alert('Submitted!');
      }
    });


    this.requestForm = this.formBuilder.group({
      catalog: ['', Validators.required],
      campaign: ['', Validators.required],
      lot: ['', Validators.required],
      reference: ['', Validators.required],
      amount: ['', Validators.required],
    });
    // console.log(this.f);
    // Table
    $('#order-listing').DataTable({
      aLengthMenu: [
        [5, 10, 15, -1],
        [5, 10, 15, 'All']
      ],
      iDisplayLength: 5,
      bLengthChange: false,
      language: {
        search: 'Pesquisar por :'
      }
    });
    $('#order-listing').each(function () {
      const datatable = $(this);
      // SEARCH - Add the placeholder for Search and Turn this into in-line form control
      const searchInput = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
      searchInput.attr('placeholder', 'Pesquisar');
      // searchInput.removeClass('form-control-sm');
      // const s = datatable.closest('.dataTables_wrapper').find('.dataTables_filter').append('<button type="button" class="btn btn-primary ml-2">New Record</button>');
    });


  }



  get f() {
    return this.requestForm.controls;
  }

  setProducts() {
    alert('oi')
  }

}
