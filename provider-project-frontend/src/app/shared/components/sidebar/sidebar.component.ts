import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  moduleId: module.id,
  selector: 'app-sidebar',
  templateUrl: 'sidebar.component.html',
})

export class SidebarComponent implements OnInit {

  currentUser: any;

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  )
  {  
    this.currentUser = this.authenticationService.currentUserValue; 
  }

  ngOnInit() { }
  
  redirectHome(){
    if(this.currentUser.type_code == 1){
      this.router.navigate(['/dashboard/admin']);
    } else if(this.currentUser.type_code == 2){
      this.router.navigate(['/dashboard/manager']);
    } else if(this.currentUser.type_code == 3){
      this.router.navigate(['/dashboard/leader']);
    } else if(this.currentUser.type_code == 4){
      this.router.navigate(['/dashboard/consultant']);
    }
  }
  redirectProfile()
  {
    if(this.currentUser.type_code == 1){
      this.router.navigate(['/dashboard/admin/profile']);
    } else if(this.currentUser.type_code == 2){
      this.router.navigate(['/dashboard/manager/profile']);
    } else if(this.currentUser.type_code == 3){
      this.router.navigate(['/dashboard/leader/profile']);
    } else if(this.currentUser.type_code == 4){
      this.router.navigate(['/dashboard/consultant/profile']);
    }
  }
  redirectRequest(){
    if(this.currentUser.type_code == 1){
      this.router.navigate(['/dashboard/admin/request']);
    } else if(this.currentUser.type_code == 2){
      this.router.navigate(['/dashboard/manager/request']);
    } else if(this.currentUser.type_code == 3){
      this.router.navigate(['/dashboard/leader/request']);
    } else if(this.currentUser.type_code == 4){
      this.router.navigate(['/dashboard/consultant/request']);
    }
  }
}