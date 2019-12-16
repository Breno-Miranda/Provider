import { first } from 'rxjs/operators';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  loginBind = false;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';

  username: any[];
  password: any[];
  binds: any[];
  currentUser: any;

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
    // redirect to home if already logged in
    if (this.authenticationService.currentUserValue) {
      this.router.navigate(['/']);
    }
    this.currentUser = this.authenticationService.currentUserValue; 
  }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });

    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/dashboard';
  }

  // convenience getter for easy access to form fields
  get f() {
    return this.loginForm.controls;
  }

  // primeiro passo para verificar usuario e empresa
  checkoutAuth() {
    this.authenticationService.bind(this.f.username.value, this.f.password.value)
      .pipe(first())
      .subscribe(
        data => {
          this.binds = data.user
          this.loginBind = data.status
        },
        error => {
          this.loginBind = error.status
          this.error = error.error;
          this.loading = false;
        });
  }
  // segundo passo quando usuario verifica se tive vinculo a empresa pode se logar. 
  next(bind: Object) {

    this.loading = true;

    setTimeout(() => {
      this.submitted = true;
      // stop here if form is invalid
      if (this.loginForm.invalid) {
        return;
      }

      this.loading = true;
      this.authenticationService.login(this.f.username.value, this.f.password.value, bind)
        .pipe(first())
        .subscribe(
          data => {
            // this.router.navigate([this.returnUrl]);
            if(data.type_code == 1){
              this.router.navigate(['/dashboard/admin']);
            } else if(data.type_code == 2){
              this.router.navigate(['/dashboard/manager']);
            } else if(data.type_code == 3){
              this.router.navigate(['/dashboard/leader']);
            } else if(data.type_code == 4){
              this.router.navigate(['/dashboard/consultant']);
            }
          },
          error => {
            console.log(error)
            this.error = error.error;
            this.loading = false;
          });
    }, 1000);
  }

  resetLogin(){
    this.loginBind = false;
    this.error = '';
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }
}
