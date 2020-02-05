import { Component, OnInit } from '@angular/core';

// service
import { RequestService } from 'src/app/core/services/requets.service';

@Component({
  selector: 'app-request-timeline',
  templateUrl: './request-timeline.component.html',
  styleUrls: ['./request-timeline.component.scss']
})
export class RequestTimelineComponent implements OnInit {

  // array table 
  requests: Array<[]> = [];

  // pagination 
  itemsPerPage: number = 0;
  totalItems: any = 0;
  page: any = 1;
  previousPage: any;

  constructor(
    private requestService: RequestService
  ) { }

  ngOnInit() {
    
    this.requestService.getAll({
      pagination: true,
    }).subscribe( data => {
      this.requests = data['results'];
      this.totalItems = data['count'];
      this.itemsPerPage = data['limit'];
    }, error => {
      // informa uma mensagem de erro caso aconteca
    });

  }

  // pagination
  
  loadPage(page: number) {
    if (page !== this.previousPage) {
      this.previousPage = page;
      this.loadData(page);
    }
  }

  loadData(page) {
    this.requestService.getAll({
      pagination: true,
      page: page
    }).subscribe( data => {
      this.requests = data['results'];
      this.page = page 
      this.itemsPerPage = data['limit'];
    }, error => {
      // informa uma mensagem de erro caso aconteca
    });
  }


}
