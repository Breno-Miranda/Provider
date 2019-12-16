import { Routes } from '@angular/router';

import { LoginComponent } from '../../modules/login/login.component';
import { ForgotPasswordComponent } from '../../modules/forgot-password/forgot-password.component';

export const AuthRoutes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'forgot-password', component: ForgotPasswordComponent },
];
