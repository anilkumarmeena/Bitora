import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ModelService} from 'src/app/model.service';
import{ EnrollmentService } from 'src/app/enrollment.service';
import { User } from './user';
import { viewAttached } from '@angular/core/src/render3/instructions';

@Component({
  selector: 'app-model',
  templateUrl: './model.component.html',
})
export class ModelComponent implements OnInit {

  @ViewChild('backdrop') backdrop: ElementRef;
  @ViewChild('model_container') model_container: ElementRef;

   userModel = new User('');
 //  response = this.view();
  constructor(private modelServ: ModelService,private _enrollmentService: EnrollmentService) { }

  ngOnInit() {
    this.modelServ.init(this.backdrop, this.model_container);
  }

  hide() {
    this.modelServ.hide();
  }
  
  /*view()
  {
    this._enrollmentService.enroll2('token')
  
.subscribe((res)=>{
            return res;
        });

  }*/

   onSubmit()
  {
  // console.log(this.userModel);
  this._enrollmentService.enroll(this.userModel)
  
.subscribe((res)=>{
            console.log(res);
        });
        this.modelServ.hide();

        

  }

}
