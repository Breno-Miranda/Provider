import { Routes } from '@angular/router';
import { Error501Component } from '../error/error501/error501.component';
import { Error403Component } from '../error/error403/error403.component';
import { Error500Component } from '../error/error500/error500.component';
import { Error400Component } from '../error/error400/error400.component';
import { Error404Component } from '../error/error404/error404.component';

export const ErrorRouter: Routes = [
  { path: 'error-404', component: Error404Component },
  { path: 'error-400', component: Error400Component },
  { path: 'error-500', component: Error500Component },
  { path: 'error-403', component: Error403Component },
  { path: 'error-501', component: Error501Component },
];
