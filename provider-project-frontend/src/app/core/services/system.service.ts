import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from './authentication.service';

import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })

export class SystemService {
  
  constructor(
    private http: HttpClient,
    private authenticationService: AuthenticationService
  ) { }
  
  
  getAll() {
    return this.http.get<any[]>(`${environment.apiUrl}/api/system/info/`, {
      params: 
      {
        company_id: this.authenticationService.currentUserValue.companyId.toString(),
        user_id: this.authenticationService.currentUserValue.id.toString(),
        type_code: this.authenticationService.currentUserValue.type_code,
        is_business: this.authenticationService.currentUserValue.is_business,
        is_individual: this.authenticationService.currentUserValue.is_individual,
        is_collaborator: this.authenticationService.currentUserValue.is_collaborator,
      }
    });
  }

}

