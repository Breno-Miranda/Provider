
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-admin-layout',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})

export class AdminComponent implements OnInit {

  code: any;
  currentUser: any;

  constructor(
    private authenticationService: AuthenticationService
  )
  {  
    this.currentUser = this.authenticationService.currentUserValue; 
    this.code = this.currentUser.type_code;
  }

  ngOnInit() { }

}
