
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { UserService } from 'src/app/core/services/user.service';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { first } from 'rxjs/operators';




@Component({
  selector: 'app-permission',
  templateUrl: './permission.component.html',
  styleUrls: ['./permission.component.scss']
})
export class PermissionComponent implements OnInit {

  error: any;
  success: any;

  users: any;
  groups: any;
  permission: any;
  userPermissionForm: FormGroup;

  constructor(
    private userService: UserService,
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService) { }

  ngOnInit() {
    this.userPermissionForm = this.formBuilder.group({
      search: ['', Validators.required],
    });
    
    this.userService.getAllPermission().pipe(first()).subscribe(data => {
      this.permission = data['permission'];
      this.groups = data['groups']
      this.users = data['users'];
    });

  }

  userId: any;

  selectUser( data ){
    if( data )
    {
      this.userId = data.user;
    } else {
      console.log('user vazio')
    }

    // CHECK PERMISSION
    this.checkedPermission( data );
    // CHECK GROUPS
    this.checkedGroup( data );
  }

  selectGroup( data ){
    if( data )
    {
      this.setFinaly(this.userId , false , data.id)
    }else {
      console.log('user group')
    }
  }

  selectPermission( data ){
    if( data )
    {
      if(data.selected){
        this.setFinaly(this.userId , data.id , false)
      } 
    }else {
      console.log('user permission')
    }
  }

  checkedPermission( data ) {
    data['_user']['user_permissions'].forEach(data_user => {
      this.permission.forEach((data_permission, index) => {
        if (data_user == data_permission['id']) {
          this.permission[index]['selected'] = true;
        } 
      });
    });
  }

  checkedGroup( data ) {
    data['_user']['groups'].forEach(data_user => {
      this.groups.forEach((data_group, index) => {
        if (data_user == data_group['id']) {
          this.groups[index]['selected'] = true;
        } 
      });
    });
    console.log(this.groups)
  }

  setFinaly(user_id , permission_id , groupId){
    this.userService.setUserPermission(user_id, permission_id, groupId).pipe(first()).subscribe(data => {
      this.success = data['success']
    }, error => {
      this.error = error['error']
    });
  }



}
