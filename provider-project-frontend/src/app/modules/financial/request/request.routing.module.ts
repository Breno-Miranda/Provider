import { Routes } from '@angular/router';



import { NewComponent } from './new/new.component';

export const RequestRouter: Routes = [
    { path: 'admin/financial/requests/new', component: NewComponent},
];