import { SystemService } from '../../../core/services/system.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-manager',
  templateUrl: './manager.component.html',
  styleUrls: ['./manager.component.scss'],
  moduleId: module.id
})
export class ManagerComponent implements OnInit {


  count_business: any;
  currentUser: any;
  data: any;

  constructor(
    private systemService: SystemService,
    private router: Router,
    private authenticationService: AuthenticationService)
  { 
    this.systemService.getAll().pipe(first()).subscribe(data => {
      this.data = data;
    });
  }

  ngOnInit() {

    this.count_business = {
      title: 'Total de Lideres',
      text: 'Contagem total de usuários',
      subtext: 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI',
      value: 0
    };

  }

}
