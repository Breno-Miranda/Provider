import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManagerOrdersComponent } from './manager-orders.component';

describe('ManagerComponent', () => {
  let component: ManagerOrdersComponent;
  let fixture: ComponentFixture<ManagerOrdersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManagerOrdersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManagerOrdersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
