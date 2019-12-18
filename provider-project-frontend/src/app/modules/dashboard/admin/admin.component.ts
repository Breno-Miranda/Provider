import { SystemService } from './../../../core/services/system.service';
import { Router } from '@angular/router';
import { Component, OnInit, Injectable } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { map } from 'rxjs/operators';

export interface TypeUser {
  collaborator: string;
  individual: string;
  business: string;
}


@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss'],
  moduleId: module.id
})

export class AdminComponent implements OnInit {

  count_collaborator: any;
  count_individual: any;
  count_business: any;
  
  data;

  constructor( private systemService: SystemService)  { 
  }

  ngOnInit() {

    this.systemService.getAll().subscribe( data => {
      this.data = data
    });

    this.count_collaborator = {
      
      text: 'Colaboradores',
      subtext: 'As informações de quantidade de colaboradores. Fique atento aos numeros.',
    };

    this.count_individual = {
      text: 'Consultor(a)s',
      subtext: 'As informações de quantidade de consultor(a)s. Fique atento aos numeros.',
    };

    this.count_business = {
      text: 'Lideres',
      subtext: 'As informações de quantidade de lideres. Fique atento aos numeros.',
    };

  }
  
}