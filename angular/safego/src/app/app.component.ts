import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  template: '<address-form></address-form><question-form></question-form>',
})

export class AppComponent{
  title = 'SafeGo';
}