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
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
      }
    });
  }

  getLots() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/lot/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
      }
    });
  }

  getCampaign() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/campaign/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
      }
    });
  }

  getCatalog() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/companys/catalog/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
      }
    });
  }

  getUsers( data: any ) {

    data['company_id'] = this.authenticationService.currentUserValue.companyId;

    return this.http.get<any[]>(`${environment.apiUrl}/api/users/profile/`, {
      params: data
    });
  }

  setRequest( data: object)
  {
    data['company_id'] = this.authenticationService.currentUserValue.companyId;

    return this.http.post<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

  putRequest( data: object)
  {
    data['company_id'] = this.authenticationService.currentUserValue.companyId;
    
    return this.http.put<any[]>(`${environment.apiUrl}/api/request/`, data);
  }

}

