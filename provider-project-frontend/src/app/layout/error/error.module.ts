import { NgModule } from '@angular/core';
import { ErrorRouter } from './error.routing';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ErrorComponent } from './error.component';


@NgModule({
  declarations: [
    ErrorComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(ErrorRouter),
  ]
})

export class ErrorModule { }
