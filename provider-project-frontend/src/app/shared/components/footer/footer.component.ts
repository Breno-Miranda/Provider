import { Component } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'app-footer',
  templateUrl: 'footer.component.html'
})

export class FooterComponent {
  test: Date = new Date();

  ngOnInit = () => {

  }
}
