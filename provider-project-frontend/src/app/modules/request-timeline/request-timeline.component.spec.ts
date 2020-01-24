import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestTimelineComponent } from './request-timeline.component';

describe('RequestTimelineComponent', () => {
  let component: RequestTimelineComponent;
  let fixture: ComponentFixture<RequestTimelineComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RequestTimelineComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RequestTimelineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
