import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { RequestModule } from './request/request.module';
import { FinancialRouter } from './financial.routing.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RequestModule,
    RouterModule.forChild(FinancialRouter),
  ]
})
export class FinancialModule { }
