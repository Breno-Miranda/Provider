import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from './authentication.service';

import { User } from '../../shared/models/user';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })

export class UserService {
  
  constructor(
    private http: HttpClient,
    private authenticationService: AuthenticationService
  ) { }

  getAll() {
    return this.http.get<User[]>(`${environment.apiUrl}/api/users/all/`);
  }

  getAllPermission()
  {
    return this.http.get<User[]>(`${environment.apiUrl}/api/users/permission/`);
  }

  getUserProfile() {

    if(this.authenticationService.currentUserValue.is_business)
    {
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/business/`, {
        params: 
        {
          company_id: this.authenticationService.currentUserValue.companyId.toString(),
          user_id: this.authenticationService.currentUserValue.id.toString(),
        }
      });
    } else if(this.authenticationService.currentUserValue.is_individual){
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/individual/`, {
        params: 
        {
          company_id: this.authenticationService.currentUserValue.companyId.toString(),
          user_id: this.authenticationService.currentUserValue.id.toString(),
        }
      });
    }else if(this.authenticationService.currentUserValue.is_collaborator){
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/collaborator/`, {
        params: 
        {
          company_id: this.authenticationService.currentUserValue.companyId.toString(),
          user_id: this.authenticationService.currentUserValue.id.toString(),
        }
      });
    }
    
  }
  
  getUserSearch( search: string) {
    return this.http.get<any[]>(`${environment.apiUrl}/api/users/search/`, {
      params: 
      {
        search: search,
      }
    });
  }

  setUserPermission( obj_users: object, obj_permission: object , obj_permission_delete: object) {
    return this.http.post<any[]>(`${environment.apiUrl}/api/users/permission/`, {
        obj_permission: obj_permission,
        obj_users: obj_users,
        obj_permission_delete: obj_permission_delete
    });
  }

  setUserProfile( formData )
  {
    formData.append('user_id',  this.authenticationService.currentUserValue.id.toString())
    formData.append('company_id', this.authenticationService.currentUserValue.companyId.toString())

    if(this.authenticationService.currentUserValue.is_business)
    {
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/business/`, formData);
    } else if(this.authenticationService.currentUserValue.is_individual){
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/individual/`, formData);
    }else if(this.authenticationService.currentUserValue.is_collaborator){
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/collaborator/`, formData);
    }

  }

  upUserProfile( formData )
  {
    formData.append('user_id',  this.authenticationService.currentUserValue.id.toString())
    formData.append('company_id', this.authenticationService.currentUserValue.companyId.toString())

    if(this.authenticationService.currentUserValue.is_business)
    {
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/business/`+ formData.get('id') +'/', formData);
    } else if(this.authenticationService.currentUserValue.is_individual){
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/individual/`+ formData.get('id') +'/', formData);
    }else if(this.authenticationService.currentUserValue.is_collaborator){
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/collaborator/`+ formData.get('id') +'/', formData);
    }
  }

}