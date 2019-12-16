import { ExtractorComponent } from './extractor/extractor.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';

import { OrdersRouter } from './orders.routing.module';

import { AdminOrdersComponent } from './admin-orders/admin-orders.component';
import { ConsultantOrdersComponent } from './consultant-orders/consultant-orders.component';
import { LeaderOrdersComponent } from './leader-orders/leader-orders.component';
import { ManagerOrdersComponent } from './manager-orders/manager-orders.component';
import { TimelineComponent } from './timeline/timeline.component';

@NgModule({
  declarations: [
    AdminOrdersComponent,
    ConsultantOrdersComponent,
    LeaderOrdersComponent,
    TimelineComponent, 
    ManagerOrdersComponent,
    ExtractorComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(OrdersRouter),
    ReactiveFormsModule
  ]
})
export class OrdersModule { }
