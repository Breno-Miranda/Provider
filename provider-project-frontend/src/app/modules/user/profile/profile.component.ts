import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/core/services/user.service';
import { first } from 'rxjs/operators';
import { AuthenticationService } from 'src/app/core/services/authentication.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {


  error: any;
  permission: any;
  success: any;

  photo: any;
  anexo: any;

  userProfileForm: FormGroup;

  currentUser: any;

    constructor(
        private userService: UserService,
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private authenticationService: AuthenticationService,
        private router: Router,
    ) {
        this.currentUser = this.authenticationService.currentUserValue; 
        this.userService.getUserProfile().pipe(first()).subscribe(data => {
        this.userProfileForm.get('bankaccount_id').setValue(data['bankaccount']['id']);
        this.userProfileForm.get('contact_id').setValue(data['contact']['id']);
        this.userProfileForm.get('id').setValue(data['id']);
        this.userProfileForm.get('username').setValue(data['_user']['username']);
        this.userProfileForm.get('cnpj').setValue(data['cnpj']);
        this.userProfileForm.get('social_name').setValue(data['social_name']);
        this.userProfileForm.get('cpf').setValue(data['cpf']);
        this.userProfileForm.get('rg').setValue(data['rg']);
        this.userProfileForm.get('address').setValue(data['address']);
        this.userProfileForm.get('complement').setValue(data['complement']);
        this.userProfileForm.get('city').setValue(data['city']);
        this.userProfileForm.get('state').setValue(data['state']);
        this.userProfileForm.get('zipcode').setValue(data['zipcode']);
        this.userProfileForm.get('number').setValue(data['number']);
        this.userProfileForm.get('birthday').setValue(data['birthday']);
        this.userProfileForm.get('civil_sate').setValue(data['civil_sate']);
        this.userProfileForm.get('recommendation').setValue(data['recommendation']);
        this.userProfileForm.get('genre').setValue(data['genre']);
        this.userProfileForm.get('phone').setValue(data['contact']['phone']);
        this.userProfileForm.get('cell').setValue(data['contact']['cell']);
        this.userProfileForm.get('email').setValue(data['contact']['email']);
        this.userProfileForm.get('account').setValue(data['bankaccount']['account']);
        this.userProfileForm.get('agency').setValue(data['bankaccount']['agency']);
        this.userProfileForm.get('bank').setValue(data['bankaccount']['bank']);
        this.userProfileForm.get('type_account').setValue(data['bankaccount']['type_account']);
        this.userProfileForm.get('kind_of_person').setValue(data['bankaccount']['kind_of_person']);
        this.userProfileForm.get('about').setValue(data['about']);
        this.userProfileForm.get('full_name').setValue(data['full_name']);

      } , error => {
        this.error = error['error'];
       
        this.permission = false;
      });
    }
    

  ngOnInit(){
    this.userProfileForm = this.formBuilder.group({
      cnpj: ['', Validators.required],
      social_name: ['', Validators.required],
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
      account: ['', Validators.required],
      agency: ['', Validators.required],
      bank: ['', Validators.required],
      type_account: ['', Validators.required],
      kind_of_person: ['', Validators.required],
      anexo: ['', Validators.required],
      photo: ['', Validators.required],
      about: ['', Validators.required],
      username: ['', Validators.required],
      newpassword: ['', Validators.required],
      confpassword: ['', Validators.required],
      full_name: ['', Validators.required],
      id: ['', Validators.required],
      bankaccount_id: ['', Validators.required],
      contact_id: ['', Validators.required],
    });
    console.log(this.f);
  }

  get f() {
    return this.userProfileForm.controls;
  }

  set()
  {
    const formData = new FormData();

    formData.append('id', this.f.id.value);
    formData.append('anexo', this.f.anexo.value);
    formData.append('photo', this.f.photo.value);
    formData.append('cnpj', this.f.cnpj.value)
    formData.append('social_name', this.f.social_name.value)
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
    formData.append('account', this.f.account.value)
    formData.append('agency', this.f.agency.value)
    formData.append('bank', this.f.bank.value)
    formData.append('type_account', this.f.type_account.value)
    formData.append('kind_of_person', this.f.kind_of_person.value)
    formData.append('anexo', this.f.anexo.value)
    formData.append('photo', this.f.photo.value)
    formData.append('about', this.f.about.value)

    this.userService.setUserProfile(formData).pipe(first()).subscribe(data => {
      this.success = data['success']
    }, error => {
      this.error = error['error']
    });
  }

  up()
  {

    const formData = new FormData();
    
    formData.append('id', this.f.id.value);
    formData.append('contact_id', this.f.contact_id.value);
    formData.append('bankaccount_id', this.f.bankaccount_id.value);
    formData.append('cnpj', this.f.cnpj.value)
    formData.append('social_name', this.f.social_name.value)
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
    formData.append('account', this.f.account.value)
    formData.append('agency', this.f.agency.value)
    formData.append('bank', this.f.bank.value)
    formData.append('type_account', this.f.type_account.value)
    formData.append('kind_of_person', this.f.kind_of_person.value)
    formData.append('anexo', this.f.anexo.value)
    formData.append('photo', this.f.photo.value)
    formData.append('about', this.f.about.value)

    this.userService.upUserProfile(formData).pipe(first()).subscribe(data => {
      this.success = data['success']
    }, error => {
      this.error = error['error']
    });
  }

  onChangeAnexo(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.userProfileForm.get('anexo').setValue(file);
    }
  }

  onChangePhoto(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.userProfileForm.get('photo').setValue(file);
    }
  }

}
