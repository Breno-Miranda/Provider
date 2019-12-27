import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { RequestRouter } from './request.routing.module';
import { NewComponent } from './new/new.component';
import { TimelineComponent } from './timeline/timeline.component';
import { ExtractComponent } from './extract/extract.component';



@NgModule({
  declarations: [NewComponent, TimelineComponent, ExtractComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(RequestRouter),
  ]
})
export class RequestModule { }
