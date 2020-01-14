
import { NgModule , NO_ERRORS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { SidebarComponent } from './components/sidebar/sidebar.component';
import { FooterComponent } from './components/footer/footer.component';
import { CardsModule } from './components/widgets/cards/cards.module';
import { AdminComponent } from './components/navbar/admin/admin.component';
import { ConsultantComponent } from './components/navbar/consultant/consultant.component';
import { ManagerComponent } from './components/navbar/manager/manager.component';
import { LeaderComponent } from './components/navbar/leader/leader.component';
import { CommonComponent } from './components/navbar/common/common.component';


@NgModule({
  exports: [
    SidebarComponent,
    FooterComponent,
    AdminComponent,
    ConsultantComponent,
    ManagerComponent,
    LeaderComponent,
    CommonComponent,
  ],
  declarations: [
    SidebarComponent,
    FooterComponent,
    AdminComponent,
    ConsultantComponent,
    ManagerComponent,
    LeaderComponent,
    CommonComponent,
  ],
  imports: [
    CommonModule,
    RouterModule,
    NgbModule,
    CardsModule,
  ],
  schemas: [ NO_ERRORS_SCHEMA ]
})

export class SharedModule { }