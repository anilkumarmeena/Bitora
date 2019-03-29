import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from 'src/app/model/user';

@Injectable({
  providedIn: 'root'
})
export class EnrollmentService {

  _url='http://127.0.0.1:8000';
  constructor(private _http: HttpClient) { }

  enroll(user: User){
  
  return  this._http.post<any>(this._url,user);

  }

  enroll2(user : string)
  {
    return  this._http.post<any>(this._url,JSON.parse(user) );

  }
}
