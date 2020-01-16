import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-navbar-common',
  templateUrl: './common.component.html',
  styleUrls: ['./common.component.scss']
})
export class CommonComponent implements OnInit {
  currentUser: any;
  urlBase: any;
  display: any;

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
    this.currentUser = this.authenticationService.currentUserValue;
  }

  ngOnInit() {
    this.currentUser = this.authenticationService.currentUserValue;

    if(this.currentUser.type_code == 1){
      this.urlBase = "/dashboard/admin";
      this.display = true;
    } else if(this.currentUser.type_code == 2){
      this.urlBase = "/dashboard/manager";
      this.display = true;
    } else if(this.currentUser.type_code == 3){
      this.urlBase = "/dashboard/leader";
      this.display = false;
    } else if(this.currentUser.type_code == 4){
      this.urlBase = "/dashboard/consultant";
      this.display = false;
    }

  }

  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }


}
