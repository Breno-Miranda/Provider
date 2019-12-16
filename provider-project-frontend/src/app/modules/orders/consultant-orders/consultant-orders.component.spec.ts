import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultantOrdersComponent } from './consultant-orders.component';

describe('ConsultantComponent', () => {
  let component: ConsultantOrdersComponent;
  let fixture: ComponentFixture<ConsultantOrdersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConsultantOrdersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConsultantOrdersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
