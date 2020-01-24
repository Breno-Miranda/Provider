import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

// service 
import { RequestService } from 'src/app/core/services/requets.service';

@Component({
  selector: 'app-request-historic',
  templateUrl: './request-historic.component.html',
  styleUrls: ['./request-historic.component.scss']
})
export class RequestHistoricComponent implements OnInit {


  //  array select 
  lots: Array<[]> = [];
  campaigns: Array<[]> = [];
  catalogs: Array<[]> = [];
  users: Array<[]> = [];


  // form

  formFilter: FormGroup;

  //  array table 
  requests: Array<[]> = [];

  constructor(
    private requestService: RequestService,
    private formBuilder: FormBuilder,
  ) { }

  ngOnInit() {
    this.getRequest();
  }
  get f() {
    return this.formFilter.controls;
  }
  getRequest() {
    this.requestService.getAll()
      .subscribe((requests: any) => {
        this.requests = requests;
      }, () => { });
  }
}