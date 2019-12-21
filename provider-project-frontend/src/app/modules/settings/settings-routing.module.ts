
import { Routes } from '@angular/router';

import { LogsComponent } from './logs/logs.component';
import { PlaintComponent } from './plaint/plaint.component';
import { GeneralComponent } from './general/general.component';


export const SettingRouter: Routes = [

  {path: 'admin/settings/logs', component: LogsComponent},
  {path: 'admin/settings/plaint', component: PlaintComponent},
  {path: 'admin/settings/general', component: GeneralComponent},
  
];