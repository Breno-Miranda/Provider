import { Component, OnInit } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';
import { first } from 'rxjs/operators';
import { UserService } from 'src/app/core/services/user.service';


import { ToastrService } from 'ngx-toastr';
import { AuthenticationService } from 'src/app/core/services/authentication.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  [x: string]: any;


  consultantForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private userService: UserService,
    private toastr: ToastrService,
    private authenticationService: AuthenticationService
  ) {

    this.consultantForm = this.formBuilder.group({
      cpf: ['', Validators.required],
      rg: ['', Validators.required],
      address: ['', Validators.required],
      complement: ['', Validators.required],
      city: ['', Validators.required],
      state: ['', Validators.required],
      zipcode: ['', Validators.required],
      number: ['', Validators.required],
      birthday: ['', Validators.required],
      civil_sate: ['', Validators.required],
      recommendation: ['', Validators.required],
      genre: ['', Validators.required],
      phone: ['', Validators.required],
      cell: ['', Validators.required],
      email: ['', Validators.required],
      about: ['', Validators.required],
      full_name: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      sector: ['', Validators.required],
      type: ['', Validators.required],
      team: ['', Validators.required],

      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      matriculation: ['', Validators.required],


    });
  }

  types:any;
  teams:any;
  sectors:any;

  ngOnInit() {
    this.userService.getUser({
        type_code: 2
    }).pipe(first()).subscribe(data => {
      this.types = data['type'];
      this.teams = data['team'];
      this.sectors = data['sector'];
    }, error => {
      this.toastr.error(error['error']);
    });
  }

  get f() {
    return this.consultantForm.controls;
  }

  setFinaly() {

    var full_name = this.f.full_name.value.replace(" da ", " ").replace(" de ", " ").split(' ')

    var data = {
      'cpf': this.f.cpf.value,
      'rg': this.f.rg.value,
      'address': this.f.address.value,
      'complement': this.f.complement.value,
      'city': this.f.city.value,
      'state': this.f.state.value,
      'zipcode': this.f.zipcode.value,
      'number': this.f.number.value,
      'birthday': this.f.birthday.value,
      'civil_sate': this.f.civil_sate.value,
      'recommendation': this.f.recommendation.value,
      'full_name': this.f.full_name.value,
      'genre': this.f.genre.value,
      'phone': this.f.phone.value,
      'cell': this.f.cell.value,
      'email': this.f.email.value,
      'username': this.f.cpf.value,
      'password': "@" + full_name[0] + full_name[1] + "#",
      'first_name': full_name[0],
      'last_name': full_name[1],
      'sector': this.f.sector.value,
      'team': this.f.team.value,
      'type': this.f.type.value,
    }

    this.userService.setUser(data).pipe(first()).subscribe(data => {
      this.toastr.success(data['success']);
    }, error => {
      this.toastr.error(error['error']);
    });
  }
}