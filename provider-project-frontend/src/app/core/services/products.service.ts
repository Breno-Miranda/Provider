import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from './authentication.service';

import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })

export class ProductsService {
  
  constructor(
    private http: HttpClient,
    private authenticationService: AuthenticationService
  ) { }
  
  
  getAll() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/request/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
      }
    });
  }

  setRequest( data: object)
  {
    return this.http.post<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

  putRequest( data: object)
  {
    return this.http.put<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

}

