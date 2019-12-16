import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AuthRoutes } from './auth.routing.module';

import { RegisterModule } from '../../modules/register/register.module';

import { LoginComponent } from '../../modules/login/login.component';
import { ForgotPasswordComponent } from '../../modules/forgot-password/forgot-password.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(AuthRoutes),
    ReactiveFormsModule,
    RegisterModule
  ],
  declarations: [
    LoginComponent,
    ForgotPasswordComponent
  ]
})

export class AuthModule { }
