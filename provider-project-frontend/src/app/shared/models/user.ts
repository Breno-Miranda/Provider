export class User {
  id: number;
  company: string;
  username: string;
  email: string;
  color_primary: string;
  color_secudary: string;
  password: string;
  firstName: string;
  first_name: string;
  lastName: string;
  last_name: string;
  token?: string;
  type: number;
  type_code: string;
  is_business: string;
  is_individual: string;
  is_collaborator: string;

  _company : object;
  _type : object;
  _team : object;
  _sector : object;
}
