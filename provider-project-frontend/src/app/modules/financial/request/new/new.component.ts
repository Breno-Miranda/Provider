import { RequestService } from './../../../../core/services/requets.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { ProductsService } from 'src/app/core/services/products.service';
import { first } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';

declare var $: any;

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.scss']
})
export class NewComponent implements OnInit {
  
  [x: string]: any;

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
      reference: ['', Validators.required],
      amount: [1, Validators.required],
      size: ['', Validators.required],
      user: ['', Validators.required],
      total_amount: [0, Validators.required],
    });
  }

  

  ngOnInit() {
    this.requestService.getLots().pipe(first()).subscribe(data => {
      this.lots = data;
    });

    this.requestService.getCampaign().pipe(first()).subscribe(data => {
      this.campaigns = data;
    });

    this.requestService.getCatalog().pipe(first()).subscribe(data => {
      this.catalogs = data;
    });

    this.requestService.getUsers({type_code: 4}).pipe(first()).subscribe(data => {
      this.users = data;
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
    this.requestService.setRequest({
      lot: this.f.lot.value,
      catalog:this.f.catalog.value,
      campaign:this.f.campaign.value,
      user:this.f.user.value,
      amount:this.f.total_amount.value,
      itens: this.itens
    }).pipe(first()).subscribe(data => {
      this.toastr.success(data['success']);
      this.itens = [];
      this.f.user.setValue('');
    });
  }
}
