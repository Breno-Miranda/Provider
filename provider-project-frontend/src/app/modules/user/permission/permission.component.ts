
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
  obj_users: any = [];
  permission: any;
  obj_permission: any = [];
  obj_permission_delete: any = [];
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
    // Load the Permission
    this.loadPermission();
    // Load the users
    this.loadUsers();
  }

  loadPermission()
  {
    this.userService.getAllPermission().pipe(first()).subscribe(data => {
      this.permission = data['permission'];
    });

  }

  loadUsers()
  {
    this.userService.getAll().pipe(first()).subscribe(data => {
      this.users = data;
    });

  }

  search() {
    this.userService.getUserSearch(this.userPermissionForm.controls.search.value).pipe(first()).subscribe(data => {
      this.users = data;
    }, error => {
      console.log(error)
    });
  }

  set() {
    this.userService.setUserPermission(this.obj_users, this.obj_permission , this.obj_permission_delete).pipe(first()).subscribe(data => {
      this.success = data['success']
    }, error => {
      this.error = error['error']
    });
  }
  selectPermission() {
    this.obj_permission = [];
    this.permission.forEach(data_permission => {
      if (data_permission.selected) {
        this.obj_users.forEach(data_user => {
          this.obj_permission.push({ 'permission_id': data_permission.id, 'user_id': data_user.user_id })
        });
      } else {
        this.obj_users.forEach(data_user => {
          this.obj_permission_delete.push({ 'permission_id': data_permission.id, 'user_id': data_user.user_id })
        });
      }
    });
  }

  selectUsers(item) {
    this.obj_users = [];
    this.users.forEach(data => {
      if (data.selected) {
        this.obj_users.push({ 'user_id': data.user })
      }
    });

    this.checkedPermission(item);
  }

  checkedPermission(item) {

    item['_user']['user_permissions'].forEach(data_user => {
      this.permission.forEach((data_permission, index) => {
        if (data_user == data_permission['id']) {
          this.permission[index]['selected'] = true;
        }
      });
    });
  }
}
