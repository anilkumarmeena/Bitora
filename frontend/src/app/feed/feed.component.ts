import {Component, OnInit} from '@angular/core';
import {ModelService} from '../model.service';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html'
})
export class FeedComponent implements OnInit{
   data : any[];
   
   constructor(private model: ModelService,private httpClient: HttpClient) {

   }

  ngOnInit() {
    this.httpClient.get('http://127.0.0.1:8000/').subscribe((res : any[])=>{
    this.data= res;
    console.log(this.data);
    });
  }


  openModel() {
    this.model.show();
  }
}

export interface jason{
  id : number;
  Answers : any[];
  question : String;
  pub_date : String

}
