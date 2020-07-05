import { Component } from '@angular/core';
import { Question } from './question';
import {HttpClient} from '@angular/common/http';
 
@Component({
    selector: 'question-form',
    templateUrl: 'question-form.component.html'
})
export class QuestionFormComponent {
  constructor(private http:HttpClient) { }
  model = new Question(1, '天安门广场', '北京', '可以出行吗?');
  submitted = false;
  onSubmit() { this.submitted = true; }
  get diagnostic() { return JSON.stringify(this.model); }
  active = true;
  onAddressSubmit(addressForm:any){
    var url='http://localhost:8000/riskIndex/';
    //console.log(addressForm);
    var data = addressForm.value;
    data = this.http.post(url, data).subscribe(response => {
      alert(response['message']);
    });
  }
}