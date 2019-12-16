import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-navbar-consultant',
  templateUrl: './consultant.component.html',
  styleUrls: ['./consultant.component.scss']
})
export class ConsultantComponent implements OnInit {

  currentUser: any;

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
    this.currentUser = this.authenticationService.currentUserValue;
  }

  ngOnInit() {
    this.currentUser = this.authenticationService.currentUserValue;
  }

  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }
}
