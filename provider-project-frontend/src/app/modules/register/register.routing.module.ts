import { Routes } from '@angular/router';

import { IndividualComponent } from './individual/individual.component';
import { ProvidersComponent } from './providers/providers.component';
import { BusinessComponent } from './business/business.component';
import { ProductsComponent } from './products/products.component';

export const RegisterRouter: Routes = [
  { path: 'register/business', component: BusinessComponent },
  { path: 'register/individual', component: IndividualComponent },
  { path: 'admin/register/providers', component: ProvidersComponent },
  { path: 'admin/register/products', component: ProductsComponent },
];