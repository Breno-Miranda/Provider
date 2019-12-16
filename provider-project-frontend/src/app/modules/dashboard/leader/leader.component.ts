import { SystemService } from '../../../core/services/system.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-leader',
  templateUrl: './leader.component.html',
  styleUrls: ['./leader.component.scss'],
  moduleId: module.id
})
export class LeaderComponent implements OnInit {

 
  count_individual: any;
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

    this.count_individual = {
      title: 'Total de Consultor(a)s',
      text: 'Contagem total de usuários',
      subtext: 'Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI',
      value: 0
    };

  }

}
