import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrantaComponent } from './entranta.component';

describe('EntrantaComponent', () => {
  let component: EntrantaComponent;
  let fixture: ComponentFixture<EntrantaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EntrantaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EntrantaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
