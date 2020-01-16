import { Routes } from '@angular/router';

import { OpencloseComponent } from './openclose/openclose.component';
import { TimelineComponent } from './timeline/timeline.component';
import { ExtratcComponent } from './extratc/extratc.component';

export const BoxRouter: Routes = [
    {path: 'admin/financial/box/timeline', component: TimelineComponent},
    {path: 'admin/financial/box/open-close', component: OpencloseComponent},
    {path: 'admin/financial/box/extract', component: ExtratcComponent},
];