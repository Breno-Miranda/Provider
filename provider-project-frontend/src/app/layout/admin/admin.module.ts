import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { CardsModule } from 'src/app/shared/components/widgets/cards/cards.module';
import { RegisterModule } from 'src/app/modules/register/register.module';

import { OrdersModule } from 'src/app/modules/orders/orders.module';
import { ErrorModule } from 'src/app/modules/error/error.module';
import { UserModule } from '../../modules/user/user.module';


import { AdminComponent } from 'src/app/modules/dashboard/admin/admin.component';
import { LeaderComponent } from 'src/app/modules/dashboard/leader/leader.component';
import { ManagerComponent } from 'src/app/modules/dashboard/manager/manager.component';
import { ConsultantComponent } from 'src/app/modules/dashboard/consultant/consultant.component';


import { AdminRoutes } from './admin.routing.module';
import { SettingsModule } from 'src/app/modules/settings/settings.module';
import { FinancialModule } from 'src/app/modules/financial/financial.module';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(AdminRoutes),
    CardsModule,
    RegisterModule,
    OrdersModule,
    UserModule,
    ErrorModule,
    SettingsModule,
    FinancialModule
  ],
  declarations: [
    AdminComponent,
    LeaderComponent,
    ManagerComponent,
    ConsultantComponent,
  ]
})

export class AdminModule {}