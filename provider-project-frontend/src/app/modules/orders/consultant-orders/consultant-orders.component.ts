import { Component, OnInit } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-consultant',
  templateUrl: './consultant-orders.component.html',
  styleUrls: ['./consultant-orders.component.scss']
})
export class ConsultantOrdersComponent implements OnInit {

  constructor() { }

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
    const validationForm = $('#example-validation-form');
    validationForm.val({
      errorPlacement: function errorPlacement(error, element) {
        element.before(error);
      },
      rules: {
        confirm: {
          equalTo: '#password'
        }
      }
    });
    validationForm.children('div').steps({
      headerTag: 'h3',
      bodyTag: 'section',
      transitionEffect: 'slideLeft',
      onStepChanging(event, currentIndex, newIndex) {
        validationForm.val({
          ignore: [':disabled', ':hidden']
        });
        return validationForm.val();
      },
      onFinishing(event, currentIndex) {
        validationForm.val({
          ignore: [':disabled']
        });
        return validationForm.val();
      },
      onFinished(event, currentIndex) {
        window.alert('Submitted!');
      }
    });
    const verticalForm = $('#example-vertical-wizard');
    verticalForm.children('div').steps({
      headerTag: 'h3',
      bodyTag: 'section',
      transitionEffect: 'slideLeft',
      stepsOrientation: 'vertical',
      onFinished(event, currentIndex) {
        window.alert('Submitted!');
      }
    });

    // Table
    $('#order-listing').DataTable({
      aLengthMenu: [
        [5, 10, 15, -1],
        [5, 10, 15, 'All']
      ],
      iDisplayLength: 5,
      bLengthChange: false,
      language: {
        search: 'Sort By :'
      }
    });
    $('#order-listing').each(function() {
      const datatable = $(this);
      // SEARCH - Add the placeholder for Search and Turn this into in-line form control
      const searchInput = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
      searchInput.attr('placeholder', 'Sort');
      // searchInput.removeClass('form-control-sm');
      const s = datatable.closest('.dataTables_wrapper').find('.dataTables_filter').append('<button type="button" class="btn btn-primary ml-2">New Record</button>');
    });

    const fixedColumnTable = $('#fixed-column').DataTable({
      aLengthMenu: [
        [5, 10, 15, -1],
        [5, 10, 15, 'All']
      ],
      columnDefs: [{
        orderable: false,
        targets: [1]
      }],
      fixedHeader: {
        header: false,
        footer: true
      },
      scrollY: 300,
      scrollX: true,
      scrollCollapse: true,
      bAutoWidth: false,
      paging: false,
      fixedColumns: true,
      iDisplayLength: 10,
      bLengthChange: true,
      language: {
        search: 'Sort By :'
      }
    });
    $('#fixed-column').each(function() {
      const datatable = $(this);
      // SEARCH - Add the placeholder for Search and Turn this into in-line form control
      const searchInput = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
      searchInput.attr('placeholder', 'Sort');
      // searchInput.removeClass('form-control-sm');
      const s = datatable.closest('.dataTables_wrapper').find('.dataTables_filter').append('<button type="button" class="btn btn-primary ml-2">New Record</button>');
    });
    $('#fixed-column_wrapper').resize(() => {
      fixedColumnTable.draw();
    });
  }

}
