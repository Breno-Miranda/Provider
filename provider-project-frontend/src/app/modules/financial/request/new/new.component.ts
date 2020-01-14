import { RequestService } from './../../../../core/services/requets.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { ProductsService } from 'src/app/core/services/products.service';
import { first } from 'rxjs/operators';

declare var $: any;

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.scss']
})
export class NewComponent implements OnInit {
  [x: string]: any;

  
  requestForm: FormGroup;

  constructor(
     private formBuilder: FormBuilder,
     private productsService: ProductsService,
     private requestService: RequestService,
  ) {
    this.requestForm = this.formBuilder.group({
      catalog: ['', Validators.required],
      campaign: ['', Validators.required],
      lot: ['', Validators.required],
      reference: ['', Validators.required],
      amount: [1, Validators.required],
      size: ['', Validators.required],
      user: ['', Validators.required],
      
    });
  }


  lots: any;

  ngOnInit() {

    this.requestService.getLots().pipe(first()).subscribe(data => {
      this.lots = data;
    });
  
  }


  itens : Array<object> = [];

  searchProducts() {
    this.productsService.getSearch( {
      search: this.f.reference.value
    } ).pipe(first()).subscribe(data => {

      data['results']['amount'] = this.f.amount.value
      data['results']['size'] = this.f.size.value
      data['results']['total_price'] = this.f.amount.value * data['results']['sale_price']


      this.itens.push(data['results']);
    });

    console.log(this.itens)
  }

  get f() {
    return this.requestForm.controls;
  }


  

}
