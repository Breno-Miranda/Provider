import { Routes } from '@angular/router';

import { AdminComponent } from 'src/app/modules/dashboard/admin/admin.component';
import { LeaderComponent } from 'src/app/modules/dashboard/leader/leader.component';
import { ManagerComponent } from 'src/app/modules/dashboard/manager/manager.component';
import { ConsultantComponent } from 'src/app/modules/dashboard/consultant/consultant.component';


import { RequestComponent } from 'src/app/modules/request/request.component';
import { RequestTimelineComponent } from 'src/app/modules/request-timeline/request-timeline.component';
import { RequestHistoricComponent } from 'src/app/modules/request-historic/request-historic.component';

export const AdminRoutes: Routes = [
  {path: '', component: AdminComponent},
  {path: 'admin', component: AdminComponent},
  {path: 'manager', component: ManagerComponent},
  {path: 'leader', component: LeaderComponent},
  {path: 'consultant', component: ConsultantComponent},

  // create new-found request
  { path: 'admin/financial/requests/new-found', component: RequestComponent},
  { path: 'manager/financial/requests/new-found', component: RequestComponent},
  { path: 'leader/financial/requests/new-found', component: RequestComponent},
  { path: 'consultant/financial/requests/new-found', component: RequestComponent},
  // timeline the request
  { path: 'admin/financial/requests/timeline', component: RequestTimelineComponent},
  { path: 'manager/financial/requests/timeline', component: RequestTimelineComponent},
  { path: 'leader/financial/requests/timeline', component: RequestTimelineComponent},
  { path: 'consultant/financial/requests/timeline', component: RequestTimelineComponent},

   // Historic the request
   { path: 'admin/financial/requests/historic', component: RequestHistoricComponent},
   { path: 'manager/financial/requests/historic', component: RequestHistoricComponent},
   { path: 'leader/financial/requests/historic', component: RequestHistoricComponent},
   { path: 'consultant/financial/requests/historic', component: RequestHistoricComponent},
 
];