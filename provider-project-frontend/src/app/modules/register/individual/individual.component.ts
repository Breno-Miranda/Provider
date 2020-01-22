import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-individual',
  templateUrl: './individual.component.html',
  styleUrls: ['./individual.component.scss']
})
export class IndividualComponent implements OnInit {

  
  formRegister: FormGroup;
  error: any;
  success: any;
  loading = false;
  data: any;
  
  constructor(
    private route: ActivatedRoute,
    private formBuilder: FormBuilder,
    private router: Router,
    private authenticationService: AuthenticationService
  ) {}


  // convenience getter for easy access to form fields
  get f() {
    return this.formRegister.controls;
  }

  ngOnInit() {

    this.formRegister = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
      password_confirm: ['', Validators.required],
    });


    if(this.route.snapshot.queryParams['uid']){
      console.log(this.route.snapshot.queryParams['uid']);

      this.authenticationService.checkCompanyToken(this.route.snapshot.queryParams['uid'])
      .pipe(first())
      .subscribe(
      data => {
        console.log(data)
      },
      error => {
        console.log(error)
      });

    } else {
      console.log('token vazio')
    }
    
   

  }


}
