import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';


import { CardsModule } from 'src/app/shared/components/widgets/cards/cards.module';
import { RegisterModule } from 'src/app/modules/register/register.module';

import { ErrorModule } from 'src/app/modules/error/error.module';
import { UserModule } from '../../modules/user/user.module';


import { AdminComponent } from 'src/app/modules/dashboard/admin/admin.component';
import { LeaderComponent } from 'src/app/modules/dashboard/leader/leader.component';
import { ManagerComponent } from 'src/app/modules/dashboard/manager/manager.component';
import { ConsultantComponent } from 'src/app/modules/dashboard/consultant/consultant.component';


import { AdminRoutes } from './admin.routing.module';
import { SettingsModule } from 'src/app/modules/settings/settings.module';


import { RequestComponent } from 'src/app/modules/request/request.component';
import { RequestTimelineComponent } from 'src/app/modules/request-timeline/request-timeline.component';
import { RequestHistoricComponent } from 'src/app/modules/request-historic/request-historic.component';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
    RouterModule.forChild(AdminRoutes),
    CardsModule,
    RegisterModule,
    UserModule,
    ErrorModule,
    SettingsModule,
  ],
  declarations: [
    AdminComponent,
    LeaderComponent,
    ManagerComponent,
    ConsultantComponent,
    RequestComponent,
    RequestTimelineComponent,
    RequestHistoricComponent
  ]
})

export class AdminModule {}