import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-stretch-card',
  templateUrl: './stretch-card.component.html',
  styleUrls: ['./stretch-card.component.scss']
})
export class StretchCardComponent implements OnInit {
 
  query: any;
  data: any;

  @Input() Query;
  @Input() Data;

  constructor() {}

  ngOnInit() { 
    this.query = this.Query; 
    this.data = this.Data; 
    // console.log(this.Data)
  }
}
