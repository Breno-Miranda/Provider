import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-error403',
  templateUrl: './error403.component.html',
  styleUrls: ['./error403.component.scss']
})
export class Error403Component implements OnInit {

  currentUser: any;

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  )
  {  
    this.currentUser = this.authenticationService.currentUserValue; 
  }

  ngOnInit() {
    
  }


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

}
