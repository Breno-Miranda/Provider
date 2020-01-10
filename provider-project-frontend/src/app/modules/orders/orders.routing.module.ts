import { Routes } from '@angular/router';

import { ConsultantOrdersComponent } from './consultant-orders/consultant-orders.component';
import { LeaderOrdersComponent } from './leader-orders/leader-orders.component';
import { ManagerOrdersComponent } from './manager-orders/manager-orders.component';

export const OrdersRouter: Routes = [
  { path: 'consultant-orders', component: ConsultantOrdersComponent },
  { path: 'leader-orders', component: LeaderOrdersComponent },
  { path: 'manager-orders', component: ManagerOrdersComponent }
];
