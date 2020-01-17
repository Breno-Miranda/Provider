import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';
import { UserRouter } from './user-routing.module';
import { ProfileComponent } from './profile/profile.component';
import { PermissionComponent } from './permission/permission.component';
import { ManagerComponent } from './manager/manager.component';

import { ConsultantComponent } from './consultant/consultant.component';
import { InputFilterPipe } from 'src/app/shared/pipe/inputfilter.pipe';
import { LeaderComponent } from './leader/leader.component';
import { UserComponent } from './user.component';
import { AdminComponent } from './admin/admin.component';


@NgModule({
  declarations: [
   ProfileComponent,
   PermissionComponent,
   ManagerComponent,
   InputFilterPipe,
   LeaderComponent,
   ConsultantComponent,
   UserComponent,
   AdminComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(UserRouter),
    ReactiveFormsModule
  ]
})

export class UserModule { }

