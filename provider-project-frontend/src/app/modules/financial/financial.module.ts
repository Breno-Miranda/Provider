import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { FinancialRouter } from './financial.routing.module';
import { RequestModule } from './request/request.module';
import { BoxModule } from './box/box.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RequestModule,
    RouterModule.forChild(FinancialRouter),
    BoxModule,
  ]
})
export class FinancialModule { }
