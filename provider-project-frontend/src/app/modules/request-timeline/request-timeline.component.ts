import { Component, OnInit } from '@angular/core';

// service
import { RequestService } from 'src/app/core/services/requets.service';

@Component({
  selector: 'app-request-timeline',
  templateUrl: './request-timeline.component.html',
  styleUrls: ['./request-timeline.component.scss']
})
export class RequestTimelineComponent implements OnInit {

  requests: any;

  constructor(
    private requestService: RequestService
  ) { }

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
