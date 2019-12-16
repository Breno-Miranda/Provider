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
      title: 'Colaboradores',
      text: 'Contagem Total de Colaboradores',
      subtext: 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI',
    };

    this.count_individual = {
      title: 'Consultor(a)s',
      text: 'Contagem Total de Consultor(a)s',
      subtext: 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI',
    };

    this.count_business = {
      title: 'Lideres',
      text: 'Contagem Total de Lideres',
      subtext: 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI',
    };

  }
  
}