import { Routes } from '@angular/router';

import { IndividualComponent } from './individual/individual.component';
import { ProvidersComponent } from './providers/providers.component';
import { BusinessComponent } from './business/business.component';
import { ProductsComponent } from './products/products.component';

export const RegisterRouter: Routes = [
  { path: 'auth/register/user/business', component: BusinessComponent },
  { path: 'auth/register/user/individual', component: IndividualComponent },
];