

import { Routes } from '@angular/router';


import { ProfileComponent } from './profile/profile.component';
import { PermissionComponent } from './permission/permission.component';
import { ManagerComponent } from './manager/manager.component';
import { LeaderComponent } from './leader/leader.component';
import { ConsultantComponent } from './consultant/consultant.component';


export const UserRouter: Routes = [
  { path: 'admin/profile', component: ProfileComponent },
  { path: 'manager/profile', component: ProfileComponent },
  { path: 'leader/profile', component: ProfileComponent },
  { path: 'consultant/profile', component: ProfileComponent },
  { path: 'admin/register/manager', component: ManagerComponent },
  { path: 'admin/register/leader', component: LeaderComponent },
  { path: 'admin/register/consultant', component: ConsultantComponent },
  // Permission
  { path: 'admin/permission', component: PermissionComponent },
];


