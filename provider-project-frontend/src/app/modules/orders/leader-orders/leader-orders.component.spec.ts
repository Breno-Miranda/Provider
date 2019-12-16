import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LeaderOrdersComponent } from './leader-orders.component';

describe('LeaderComponent', () => {
  let component: LeaderOrdersComponent;
  let fixture: ComponentFixture<LeaderOrdersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LeaderOrdersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LeaderOrdersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
