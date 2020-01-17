
import { Routes } from '@angular/router';

import { ConsultantComponent } from './consultant/consultant.component';
import { PermissionComponent } from './permission/permission.component';
import { ProfileComponent } from './profile/profile.component';
import { ManagerComponent } from './manager/manager.component';
import { LeaderComponent } from './leader/leader.component';
import { AdminComponent } from './admin/admin.component';


export const UserRouter: Routes = [

  { path: 'admin/profile', component: ProfileComponent },
  { path: 'manager/profile', component: ProfileComponent },
  { path: 'leader/profile', component: ProfileComponent },
  { path: 'consultant/profile', component: ProfileComponent },

  { path: 'admin/register/manager', component: ManagerComponent },
  { path: 'admin/register/leader', component: LeaderComponent },
  { path: 'admin/register/consultant', component: ConsultantComponent },
  { path: 'admin/register/admin', component: AdminComponent },

  { path: 'manager/register/manager', component: ManagerComponent },
  { path: 'manager/register/leader', component: LeaderComponent },
  { path: 'manager/register/consultant', component: ConsultantComponent },


  { path: 'leader/register/leader', component: LeaderComponent },
  { path: 'leader/register/consultant', component: ConsultantComponent },

  { path: 'admin/permission', component: PermissionComponent },
];


