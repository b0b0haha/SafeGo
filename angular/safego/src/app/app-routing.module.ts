import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component'
import { MapGeoComponent } from './components/map-geo/map-geo.component'


const routes: Routes = [
  {
    path:'home', component : HomeComponent
  },

  {
    path:'search_by_map', component : MapGeoComponent
  },

  {
    path:'**', redirectTo : 'home'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
