import { Routes } from '@angular/router';

import { AdminComponent } from 'src/app/modules/dashboard/admin/admin.component';
import { LeaderComponent } from 'src/app/modules/dashboard/leader/leader.component';
import { ManagerComponent } from 'src/app/modules/dashboard/manager/manager.component';
import { ConsultantComponent } from 'src/app/modules/dashboard/consultant/consultant.component';

export const AdminRoutes: Routes = [
  {path: '', component: AdminComponent},
  {path: 'admin', component: AdminComponent},
  {path: 'manager', component: ManagerComponent},
  {path: 'leader', component: LeaderComponent},
  {path: 'consultant', component: ConsultantComponent},
];