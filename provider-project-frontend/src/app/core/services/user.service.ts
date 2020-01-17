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


  getUserSearch(search: string) {
    return this.http.get<any[]>(`${environment.apiUrl}/api/users/search/`, {
      params:
      {
        search: search,
      }
    });
  }

  getAll() {
    return this.http.get<User[]>(`${environment.apiUrl}/api/users/all/`, {
      params:
      {
        company_id: this.authenticationService.currentUserValue.company.toString(),
      }
    });
  }

  getAllPermission() {
    return this.http.get<User[]>(`${environment.apiUrl}/api/users/permission/`, {
      params:
      {
        company_id: this.authenticationService.currentUserValue.company.toString(),
      }
    });
  }


  // PERMISSAO USER

  setUserPermission(user_id: any, permission_id: any, group_id: any) {
    return this.http.post<any[]>(`${environment.apiUrl}/api/users/permission/`, {
      user_id: user_id,
      permission_id: permission_id,
      group_id: group_id
    });
  }

  // PERFIL

  getUserProfile() {

    if (this.authenticationService.currentUserValue.is_business) {
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/business/`, {
        params:
        {
          company_id: this.authenticationService.currentUserValue.company.toString(),
          user_id: this.authenticationService.currentUserValue.user.toString(),
        }
      });
    } else if (this.authenticationService.currentUserValue.is_individual) {
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/individual/`, {
        params:
        {
          company_id: this.authenticationService.currentUserValue.company.toString(),
          user_id: this.authenticationService.currentUserValue.user.toString(),
        }
      });
    } else if (this.authenticationService.currentUserValue.is_collaborator) {
      return this.http.get<any[]>(`${environment.apiUrl}/api/users/collaborator/`, {
        params:
        {
          company_id: this.authenticationService.currentUserValue.company.toString(),
          user_id: this.authenticationService.currentUserValue.user.toString(),
        }
      });
    }

  }

  setUserProfile(formData) {
    formData.append('user_id', this.authenticationService.currentUserValue.user.toString())
    formData.append('company_id', this.authenticationService.currentUserValue.company.toString())

    if (this.authenticationService.currentUserValue.is_business) {
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/business/`, formData);
    } else if (this.authenticationService.currentUserValue.is_individual) {
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/individual/`, formData);
    } else if (this.authenticationService.currentUserValue.is_collaborator) {
      return this.http.post<any[]>(`${environment.apiUrl}/api/users/collaborator/`, formData);
    }

  }

  upUserProfile(formData) {
    formData.append('user_id', this.authenticationService.currentUserValue.user.toString())
    formData.append('company_id', this.authenticationService.currentUserValue.company.toString())

    if (this.authenticationService.currentUserValue.is_business) {
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/business/` + formData.get('id') + '/', formData);
    } else if (this.authenticationService.currentUserValue.is_individual) {
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/individual/` + formData.get('id') + '/', formData);
    } else if (this.authenticationService.currentUserValue.is_collaborator) {
      return this.http.put<any[]>(`${environment.apiUrl}/api/users/collaborator/` + formData.get('id') + '/', formData);
    }
  }

  // create user bind profile 

  // listando usuario
  getUser(data: any) {
    data['company_id'] = this.authenticationService.currentUserValue.company;
    return this.http.get<any[]>(`${environment.apiUrl}/api/users/`, {
      params: data
    });
  }
  //  criando usuario. 
  setUser(data: object) {
    data['user_link'], this.authenticationService.currentUserValue.user.toString();
    data['company'] = this.authenticationService.currentUserValue.company.toString();
    return this.http.post<any[]>(`${environment.apiUrl}/api/users/`, data);
  }


}