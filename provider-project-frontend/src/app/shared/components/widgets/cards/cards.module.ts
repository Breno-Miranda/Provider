import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardsComponent } from './cards.component';
import { ChartCardComponent } from './chart-card/chart-card.component';
import { SimpleCardComponent } from './simple-card/simple-card.component';
import { GreetingsComponent } from './greetings/greetings.component';
import { StretchCardComponent } from './stretch-card/stretch-card.component';

@NgModule({
  exports: [
    CardsComponent,
    ChartCardComponent,
    SimpleCardComponent,
    GreetingsComponent,
    StretchCardComponent
  ],
  declarations: [
    CardsComponent,
    ChartCardComponent,
    SimpleCardComponent,
    GreetingsComponent,
    StretchCardComponent
  ],
  imports: [
    CommonModule
  ]
})
export class CardsModule { }
