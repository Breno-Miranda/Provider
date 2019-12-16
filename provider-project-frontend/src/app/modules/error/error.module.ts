import { NgModule } from '@angular/core';
import { ErrorRouter } from './error.routing';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { Error404Component } from './error404/error404.component';
import { Error400Component } from './error400/error400.component';
import { Error500Component } from './error500/error500.component';
import { Error403Component } from './error403/error403.component';
import { Error501Component } from './error501/error501.component';

@NgModule({
  declarations: [Error404Component, Error400Component, Error500Component, Error403Component, Error501Component],
  imports: [
    CommonModule,
    RouterModule.forChild(ErrorRouter),
  ]
})

export class ErrorModule { }
