import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from './authentication.service';

import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })

export class RequestService {
  
  constructor(
    private http: HttpClient,
    private authenticationService: AuthenticationService
  ) { }
  
  
  getAll() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/request/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.company.toString(),
      }
    });
  }

  getRequest( data: any ) {
    data['company_id'] = this.authenticationService.currentUserValue.company;

    return this.http.get<any[]>(`${environment.apiUrl}/api/request/`, {
      params: data
    });
  }

  setRequest( data: object)
  {
    data['company'] = this.authenticationService.currentUserValue.company.toString();
    data['user_bind_typeit'] = this.authenticationService.currentUserValue.id.toString();

    return this.http.post<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

  putRequest( data: object)
  {
    data['company_id'] = this.authenticationService.currentUserValue.company.toString();
    data['user_bind_typeit'] = this.authenticationService.currentUserValue.id.toString();
    return this.http.put<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

}

