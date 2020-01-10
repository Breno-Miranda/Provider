import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { NewComponent } from './new/new.component';
import { RequestRouter } from './request.routing.module';
import { ExtractComponent } from './extract/extract.component';
import { TimelineComponent } from './timeline/timeline.component';


@NgModule({
  declarations: [
    NewComponent,
    TimelineComponent,
    ExtractComponent],
  imports: [
    CommonModule,
    NgbModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forChild(RequestRouter),
  ]
})
export class RequestModule { }
