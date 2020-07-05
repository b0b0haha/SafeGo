import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { QuestionFormComponent } from './question-answering/question-form.component';
import { AddressFormComponent } from './question-answering/address-form.component';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    QuestionFormComponent,
    AddressFormComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
