import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestHistoricComponent } from './request-historic.component';

describe('RequestHistoricComponent', () => {
  let component: RequestHistoricComponent;
  let fixture: ComponentFixture<RequestHistoricComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RequestHistoricComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RequestHistoricComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
