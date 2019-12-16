import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-greetings',
  templateUrl: './greetings.component.html',
  styleUrls: ['./greetings.component.scss']
})
export class GreetingsComponent implements OnInit {

  d: any;
  hour: any;
  titleIn: any;
  subtitleIn: any;
  currentUser: any;

  constructor(
    private authenticationService: AuthenticationService)
  { 
    this.currentUser = this.authenticationService.currentUserValue;
    this.d = new Date();
    this.hour = this.d.getHours();

    if(this.hour < 5)
    {
      this.titleIn = "Boa Noite";
      this.subtitleIn = "Seu ambiente está pronto para seu trabalho. Aproveite, tenha uma ótima experiencia."
    }
    else
    if(this.hour < 8)
    {
      this.titleIn = "Bom Dia";
      this.subtitleIn = "Seu ambiente está pronto para seu trabalho. Aproveite, tenha uma ótima experiencia."
    }
    else
    if(this.hour < 12)
    {
      this.titleIn = "Bom Dia!";
      this.subtitleIn = "Seu ambiente está pronto para seu trabalho. Aproveite, tenha uma ótima experiencia."
    }
    else
    if(this.hour < 18)
    {
      this.titleIn = "Boa tarde";
      this.subtitleIn = "Seu ambiente está pronto para seu trabalho. Aproveite, tenha uma ótima experiencia."
    }
    else
    {
      this.titleIn = "Boa noite";
      this.subtitleIn = "Seu ambiente está pronto para seu trabalho. Aproveite, tenha uma ótima experiencia."
    }
 
  }

  ngOnInit() {

  }
  
}