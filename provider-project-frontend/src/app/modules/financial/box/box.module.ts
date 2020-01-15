import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BoxRouter } from './box.routing.module';

import { OpencloseComponent } from './openclose/openclose.component';
import { TimelineComponent } from './timeline/timeline.component';
import { ExtratcComponent } from './extratc/extratc.component';
import { BoxComponent } from './box.component';

@NgModule({
  declarations: [TimelineComponent, OpencloseComponent, ExtratcComponent, BoxComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(BoxRouter),
  ]
})
export class BoxModule { }