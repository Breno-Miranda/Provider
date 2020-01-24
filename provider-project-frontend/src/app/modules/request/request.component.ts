
import { first } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

// service
import { ProductsService } from 'src/app/core/services/products.service';
import { RequestService } from 'src/app/core/services/requets.service';

declare var $: any;

@Component({
  selector: 'app-request',
  templateUrl: './request.component.html',
  styleUrls: ['./request.component.scss']
})

export class RequestComponent implements OnInit {
 
  [x: string]: any;


  submitted = false;
  requestForm: FormGroup;

  error: any;
  success: any;

  // itens e total.
  itens: Array<[]> = [];
  total = 0;

  //  array select 
  lots: Array<[]> = [];
  campaigns: Array<[]> = [];
  catalogs: Array<[]> = [];
  users: Array<[]> = [];

  constructor(
     private formBuilder: FormBuilder,
     private productsService: ProductsService,
     private requestService: RequestService,
     private toastr: ToastrService
  ) {
    this.requestForm = this.formBuilder.group({
      catalog: ['', Validators.required],
      campaign: ['', Validators.required],
      lot: ['', Validators.required],
      reference: ['',],
      amount: [1, Validators.required],
      size: ['', ],
      total_amount: [0,],
      profile: ['', Validators.required],
    });
  }

  
  ngOnInit() {
    this.requestService.getRequest({
      type_code:4
    }).pipe(first()).subscribe(data => {
      this.lots = data['lots']
      this.campaigns = data['campaigns']
      this.catalogs = data['catalogs']
      this.users = data['users']
    });
  }

  searchProducts() {
    this.productsService.getSearch( {
      search: this.f.reference.value
    } ).pipe(first()).subscribe(data => {
        data['results']['amount'] = this.f.amount.value
        data['results']['size']   = this.f.size.value
        data['results']['total']  = (this.f.amount.value * data['results']['sale_price']).toFixed(2);
        this.total += parseFloat(data['results']['total']);
        this.f.total_amount.setValue( parseFloat(this.total.toFixed(2)) ) 
        this.f.amount.setValue(1);
        this.f.size.setValue('');
        this.f.reference.setValue('');
        this.itens.push(data['results']);
    });
  }

  get f() {
    return this.requestForm.controls;
  }

  setFinaly()
  {

    this.submitted = true;

    // stop here if form is invalid
    if (this.requestForm.invalid) {
      return;
    }


    this.requestService.setRequest({
      lot: this.f.lot.value,
      catalog:this.f.catalog.value,
      profile:this.f.profile.value,
      campaign:this.f.campaign.value,
      amount:this.f.total_amount.value,
      itens: this.itens
    }).pipe(first()).subscribe(data => {
      this.toastr.success(data['success']);
      this.itens = [];
      this.f.user.setValue('');
    });
  }

}
