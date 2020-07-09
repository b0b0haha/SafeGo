import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MapGeoComponent } from './map-geo.component';

describe('MapGeoComponent', () => {
  let component: MapGeoComponent;
  let fixture: ComponentFixture<MapGeoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MapGeoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MapGeoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
