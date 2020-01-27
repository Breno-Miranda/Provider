import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
pdfMake.vfs = pdfFonts.pdfMake.vfs;


// service 
import { RequestService } from 'src/app/core/services/requets.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-request-historic',
  templateUrl: './request-historic.component.html',
  styleUrls: ['./request-historic.component.scss']
})
export class RequestHistoricComponent implements OnInit {


  //  array select 
  lots: Array<[]> = [];
  campaigns: Array<[]> = [];
  catalogs: Array<[]> = [];
  users: Array<[]> = [];


  // form
  formFilter: FormGroup;

  //  array table 
  requests: Array<[]> = [];

  constructor(
    private requestService: RequestService,
    private formBuilder: FormBuilder,
  ) {
    this.formFilter = this.formBuilder.group({
      catalog: ['', Validators.required],
      campaign: ['', Validators.required],
      lot: ['', Validators.required],
      profile: ['', Validators.required],
    });
  }

  ngOnInit() {
    this.getSelectValues();
    this.getRequest();
  }

  get f() {
    return this.formFilter.controls;
  }

  getRequest() {
    this.requestService.getAll()
      .subscribe((requests: any) => {
        this.requests = requests;
      }, () => { });
  }

  filter() {}

  getSelectValues() {
    this.requestService.getRequest({
      type_code:4
    }).pipe(first()).subscribe(data => {
      this.lots = data['lots']
      this.campaigns = data['campaigns']
      this.catalogs = data['catalogs']
      this.users = data['users']
    });
  }

  generatePdf() {

    var contentX = [
     {text: 'Aviso de Pedido\n\n',  bold: true,  alignment: 'center'},
     {
       columns: [
         {
           type: 'none',
           ul: [
             { text: 'Informações da Consultora(o):\n\n', bold: true },
           ],
         },
         {
           type: 'none',
           ul: [
             { text: 'Informações do Pedido:\n\n', bold: true },
           ]
         }
       ]
     },
     {
       columns: [
         {
           type: 'none',
           ul: [
             'Nome:',
             'CPF',
             'Telefone:',
             'Endereco:',
             'Cidade:',
             'Bairro:',
             'CEP:\n\n',
           ]
         },
         {
           type: 'none',
           ul: [
             'Pedido:',
             'Catalogo:',
             'Revista:',
             'Lider:',
             'Valor:',
             'Data:',
           ]
         }
       ]
     },
     {text: 'Tabela de Itens:\n\n', fontSize: 14, bold: true},
     {
       table: {
         headerRows: 1,
         widths: [ '*', 'auto', 100, '*', '*',  '*',  '*' ],
         body: [
           [{text: 'Referencia', bold: true },  { text: 'Tm', bold: true },  { text: 'Descricao', bold: true },  { text: 'Pagina', bold: true }, { text: 'Qtd', bold: true }, { text: 'Unitario', bold: true }, { text: 'Total', bold: true }],
           [ 'Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 4', 'Value 4', 'Value 4' ],
         ]
       }
     },
     {text: '\n\n'},
     { qr: 'https://sivendiweb.com.br/app', fit: '70' },
   ]

  // {text: 'Informações da Consultora(o)',  bold: true,  alignment: 'left'},
    
   const documentDefinition = { content: contentX };
   pdfMake.createPdf(documentDefinition).open({}, window);
 }


}