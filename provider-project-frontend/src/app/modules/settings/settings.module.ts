import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { SettingRouter } from './settings-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { LogsComponent } from './logs/logs.component';
import { PlaintComponent } from './plaint/plaint.component';
import { GeneralComponent } from './general/general.component';
import { SettingsComponent } from './settings.component';

@NgModule({
  declarations: [PlaintComponent, GeneralComponent, LogsComponent, SettingsComponent],
  imports: [
    CommonModule,
    FormsModule,
    NgbModule,
    RouterModule.forChild(SettingRouter),
    ReactiveFormsModule
  ]
})
export class SettingsModule { }