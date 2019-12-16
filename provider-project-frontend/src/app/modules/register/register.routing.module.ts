import { Routes } from '@angular/router';
import { BusinessComponent } from './business/business.component';
import { IndividualComponent } from './individual/individual.component';


export const RegisterRouter: Routes = [
  { path: 'register/business', component: BusinessComponent },
  { path: 'register/individual', component: IndividualComponent }
];
