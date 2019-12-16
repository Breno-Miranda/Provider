import { first } from 'rxjs/operators';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AuthenticationService } from './../../core/services/authentication.service';


@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})

export class ForgotPasswordComponent implements OnInit {

  loginForm: FormGroup;
  loginBind = false;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';

  email: any[];

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService
  ) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
    });

    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/dashboard';
  }

  // convenience getter for easy access to form fields
  get f() {
    return this.loginForm.controls;
  }

  onSubmit()
  {
    this.submitted = true;
    // stop here if form is invalid
    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;
    this.authenticationService.ForgotPassword(this.f.email.value)
    .pipe(first())
    .subscribe(
      data => {
        this.router.navigate([this.returnUrl]);
      },
      error => {
        this.error = error.error;
        this.loading = false;
      });
  }

}
