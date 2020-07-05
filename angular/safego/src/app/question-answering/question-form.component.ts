import { Component } from '@angular/core';
import { Question } from './question';
import {HttpClient} from '@angular/common/http';
 
@Component({
    selector: 'question-form',
    templateUrl: 'question-form.component.html'
})
export class QuestionFormComponent {
  constructor(private http:HttpClient) { }
  model = new Question(1, '可以出行吗?');
  submitted = false;
  onSubmit() { 
    this.submitted = true; 
  }
  get diagnostic() { 
    return JSON.stringify(this.model); 
  }
  active = true;
  onQuestionSubmit(questionForm:any){
    var url='http://localhost:8000/search_advise/';
    var data = questionForm.value;
    data = this.http.post(url, data).subscribe(response => {
      console.log(response);
      alert(response['answer']);
    });
  }
}