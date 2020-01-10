import { NgModule } from '@angular/core';
import { ErrorRouter } from './error.routing';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(ErrorRouter),
  ]
})

export class ErrorModule { }
