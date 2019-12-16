import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { RegisterRouter } from './register.routing.module';

import { BusinessComponent } from './business/business.component';
import { IndividualComponent } from './individual/individual.component';

@NgModule({
  declarations: [
    BusinessComponent,
    IndividualComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(RegisterRouter),
    ReactiveFormsModule
  ]
})
export class RegisterModule { }
