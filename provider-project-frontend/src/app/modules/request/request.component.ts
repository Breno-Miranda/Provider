
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
  
  // Form
  requestForm: FormGroup;
  requestFormSearch:  FormGroup;
  requestFormItens:  FormGroup;

  // Msm
  error: any;
  success: any;
 
  // Select 
  lots: Array<[]> = [];
  campaigns: Array<[]> = [];
  catalogs: Array<[]> = [];
  users: Array<[]> = [];

   // itens e total.
   itens: Array<[]> = [];
 
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
      amount: [1, Validators.required],
      size: ['', ],
      total_amount: [0,],
      profile: [[], Validators.required],
    });

    this.requestFormSearch = this.formBuilder.group({
      reference: ['', Validators.required],
      amount: [1, Validators.required],
      size: ['', ],
    });

    this.requestFormItens = this.formBuilder.group({
      amount: [1, Validators.required],
    });

  }

  ngOnInit() {
    this.getSelectValues();
  }

  getSelectValues() {
    this.requestService.getRequest({
      type_code:4
    }).pipe(first()).subscribe(data => {
      this.lots = data['lots']
      this.campaigns = data['campaigns']
      this.catalogs = data['catalogs']
      this.users = data['users']
    });
  }

  RecalculoTotal()
  {
    var total = 0;

    this.itens.map(value =>{
      total += Number(value['total']) 
    });

    this.f.total_amount.setValue( total.toFixed(2) ) 
  }

  searchProducts() {

    this.submitted = true;

    // stop here if form is invalid
    if (this.requestFormSearch.invalid) {
      return;
    }

    this.productsService.getSearch( {
      catalog_id: this.f.catalog.value,
      search: this.f_search.reference.value
    } ).pipe(first()).subscribe(data => {


        data['results']['amount'] = this.f_search.amount.value
        data['results']['size']   = this.f_search.size.value
        data['results']['total']  = parseFloat((this.f_search.amount.value * data['results']['sale_price']).toFixed(2));

        this.RecalculoTotal();

        this.itens.push(data['results']);

        this.toastr.success('Item "'+this.f_search.reference.value+'" adicionado com sucesso!');
      
        this.f_search.amount.setValue(1);
        this.f_search.size.setValue('');
        this.f_search.reference.setValue('');

    },
    error => {
      this.toastr.error("A referencia pesquisada não existe. Tente novamente.");
    });
  }

  get f() {
    return this.requestForm.controls;
  }

  get f_search() {
    return this.requestFormSearch.controls;
  }

  get f_edit_itens() {
    return this.requestFormItens.controls;
  }

  setEditItens( index )
  {
    var total = 0;

    this.itens.reverse()[index]['amount'] = this.f_edit_itens.amount.value
    this.itens[index]['total']  = (this.f_edit_itens.amount.value * this.itens[index]['sale_price']).toFixed(2);
    total += parseFloat(this.itens.reverse()[index]['total']);
    this.f.total_amount.setValue( (total.toFixed(2)) ) 

  }
  
  removeItens( index ){

    this.toastr.success('O Item "' + this.itens[index]['id'] + '" foi removido.');
   
    this.itens.reverse().splice(index, 1);
    
    this.RecalculoItens();
  }

  RecalculoItens()
  {
    var total = 0; 

    this.itens.forEach(data => {
      total += Number( data['amount'] * data['sale_price'] );
      this.f.total_amount.setValue( (total.toFixed(2)) ) 
    });
  }

  setFinaly()
  {

    this.RecalculoTotal();

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
      this.f.profile.setValue([]);
    });
  }



}
