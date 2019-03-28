import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ModelService} from 'src/app/model.service';
import{ EnrollmentService } from 'src/app/enrollment.service';
import { User } from './user';

@Component({
  selector: 'app-model',
  templateUrl: './model.component.html',
})
export class ModelComponent implements OnInit {

  @ViewChild('backdrop') backdrop: ElementRef;
  @ViewChild('model_container') model_container: ElementRef;

   userModel = new User('');

  constructor(private modelServ: ModelService,private _enrollmentService: EnrollmentService) { }

  ngOnInit() {
    this.modelServ.init(this.backdrop, this.model_container);
  }

  hide() {
    this.modelServ.hide();
  }

   onSubmit()
  {
  // console.log(this.userModel);
  this._enrollmentService.enroll(this.userModel)
  
.subscribe((res)=>{
            console.log(res);
        });

  }

}
