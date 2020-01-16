import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { FinancialRouter } from './financial.routing.module';
import { FinancialComponent } from './financial.component';
import { RequestModule } from './request/request.module';
import { BoxModule } from './box/box.module';


@NgModule({
  declarations: [
    FinancialComponent
  ],
  imports: [
    CommonModule,
    RequestModule,
    RouterModule.forChild(FinancialRouter),
    BoxModule,
  ]
})
export class FinancialModule { }
