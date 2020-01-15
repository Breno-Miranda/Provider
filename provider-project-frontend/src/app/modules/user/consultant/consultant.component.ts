import { Component, OnInit } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-consultant',
  templateUrl: './consultant.component.html',
  styleUrls: ['./consultant.component.scss']
})
export class ConsultantComponent implements OnInit {
  [x: string]: any;


  consultantForm: FormGroup;
  
  constructor(
    private formBuilder: FormBuilder,
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
      username: ['', Validators.required],
      full_name: ['', Validators.required],
    });
  }

  ngOnInit() {

  
  }

  setFinaly(){

    const formData = new FormData();

    formData.append('cpf', this.f.cpf.value)
    formData.append('rg', this.f.rg.value)
    formData.append('address', this.f.address.value)
    formData.append('complement', this.f.complement.value)
    formData.append('city', this.f.city.value)
    formData.append('state', this.f.state.value)
    formData.append('zipcode', this.f.zipcode.value)
    formData.append('number', this.f.number.value)
    formData.append('birthday', this.f.birthday.value)
    formData.append('civil_sate', this.f.civil_sate.value)
    formData.append('recommendation', this.f.recommendation.value)
    formData.append('full_name', this.f.full_name.value)
    formData.append('genre', this.f.genre.value)
    formData.append('phone', this.f.phone.value)
    formData.append('cell', this.f.cell.value)
    formData.append('email', this.f.email.value)

    this.userService.setUser(formData).pipe(first()).subscribe(data => {
      this.toastr.success(data['success']);
    }, error => {
      this.toastr.success(error['error']);
    });
  }

}
