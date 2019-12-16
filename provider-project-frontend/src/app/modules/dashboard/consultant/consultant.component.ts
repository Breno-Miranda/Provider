import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-consultant',
  templateUrl: './consultant.component.html',
  styleUrls: ['./consultant.component.scss'],
  moduleId: module.id
})
export class ConsultantComponent implements OnInit {

  data: any;
  request: any;

  constructor() {  }

  ngOnInit() {
    this.request = {
      title: 'Meus Pedidos (Cancelados)',
      text: 'Meus Pedidos (Cancelados)',
      subtext: 'Meus Pedidos (Cancelados)',
    };
    this.data = 100
  }
}
