import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArticuloCrearComponent } from './articulo-crear.component';

describe('ArticuloCrearComponent', () => {
  let component: ArticuloCrearComponent;
  let fixture: ComponentFixture<ArticuloCrearComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArticuloCrearComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArticuloCrearComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
