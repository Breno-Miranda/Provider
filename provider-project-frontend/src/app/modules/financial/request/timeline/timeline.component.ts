import { Component, OnInit } from '@angular/core';

import { RequestService } from './../../../../core/services/requets.service';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-timeline',
  templateUrl: './timeline.component.html',
  styleUrls: ['./timeline.component.scss']
})
export class TimelineComponent implements OnInit {


  requests: any;

  constructor(
    private requestService: RequestService ,
  ) {

   }

  ngOnInit() {
    this.getRequest();
  }

  getRequest() {
    this.requestService.getAll()
    .subscribe((requests: any) => {
      this.requests = requests;
    }, () => { });
  }

}
