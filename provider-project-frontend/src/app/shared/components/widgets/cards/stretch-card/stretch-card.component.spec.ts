import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StretchCardComponent } from './stretch-card.component';

describe('StretchCardComponent', () => {
  let component: StretchCardComponent;
  let fixture: ComponentFixture<StretchCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StretchCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StretchCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
