import { Routes } from '@angular/router';

import { NewComponent } from './new/new.component';
import { TimelineComponent } from './timeline/timeline.component';
import { ExtractComponent } from './extract/extract.component';

export const RequestRouter: Routes = [
    // create new request
    { path: 'admin/financial/requests/new', component: NewComponent},
    { path: 'manager/financial/requests/new', component: NewComponent},
    { path: 'leader/financial/requests/new', component: NewComponent},
    { path: 'consultant/financial/requests/new', component: NewComponent},
    // timeline the request
    { path: 'admin/financial/requests/timeline', component: TimelineComponent},
    { path: 'manager/financial/requests/timeline', component: TimelineComponent},
    { path: 'leader/financial/requests/timeline', component: TimelineComponent},
    { path: 'consultant/financial/requests/timeline', component: TimelineComponent},
    // extract the request
    { path: 'admin/financial/requests/extract', component: ExtractComponent},
    { path: 'manager/financial/requests/extract', component: ExtractComponent},
    { path: 'leader/financial/requests/extract', component: ExtractComponent},
    { path: 'consultant/financial/requests/extract', component: ExtractComponent},
];