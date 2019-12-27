import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExtratcComponent } from './extratc.component';

describe('ExtratcComponent', () => {
  let component: ExtratcComponent;
  let fixture: ComponentFixture<ExtratcComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExtratcComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExtratcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
