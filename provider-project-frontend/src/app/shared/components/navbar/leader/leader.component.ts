import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-navbar-leader',
  templateUrl: './leader.component.html',
  styleUrls: ['./leader.component.scss']
})
export class LeaderComponent implements OnInit {

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
