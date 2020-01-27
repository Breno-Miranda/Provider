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
        console.log(requests)
      }, () => { });
  }

  filter() { }

  getSelectValues() {
    this.requestService.getRequest({
      type_code: 4
    }).pipe(first()).subscribe(data => {
      this.lots = data['lots']
      this.campaigns = data['campaigns']
      this.catalogs = data['catalogs']
      this.users = data['users']
    });
  }

  generatePdf(request_id) {


    var requestPdf = [];

    this.requestService.getPrintPdf({
      'request_id': request_id
    }).subscribe(requests => {
      requestPdf = requests;

      var data = [];

      requestPdf['itens'].forEach((value, index) => {

        data[0] = [
          { text: 'Referencia', bold: true },
          { text: 'Tm', bold: true },
          { text: 'Descricao', bold: true },
          { text: 'Pagina', bold: true },
          { text: 'Qtd', bold: true },
          { text: 'Unitario', bold: true },
          { text: 'Total', bold: true }];

        data[index + 1] = [ 
          { text: value['_product']['reference'] },
          { text: value['_product']['size'] },
          { text: value['_product']['description'] },
          { text: value['_product']['page'] },
          { text: value['amount'] },
          { text: value['_product']['sale_price'] },
          { text: value['total'] }]
      });



      console.log(data);


      var contentX = [
        { text: 'Aviso de Pedido\n\n', bold: true, alignment: 'center' },
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
                'Nome:' + '  ' + requestPdf['_profile']['full_name'],
                'CPF' + '  ' + requestPdf['_profile']['cpf'],
                'Telefone:' + '  ' + requestPdf['_profile']['cell'],
                'Endereco:' + '  ' + requestPdf['_profile']['address'],
                'Cidade:' + '  ' + requestPdf['_profile']['city'],
                'Bairro:' + '  ' + requestPdf['_profile']['neighborhood'],
                'CEP:' + '  ' + requestPdf['_profile']['cep'],
              ]
            },
            {
              type: 'none',
              ul: [
                'Pedido:',
                'Catalogo: ' + '  ' + requestPdf['_catalog']['_catalog']['name'],
                'Revista:' + '  ' + requestPdf['_catalog'].reference,
                'Lider:',
                'Valor:',
                'Data:',
              ]
            }
          ]
        },
        { text: 'Tabela de Itens:\n\n', fontSize: 14, bold: true },
        {
          table: {
            headerRows: 1,
            widths: ['*', 10, 'auto', '*', '*', '*', '*'],
            body: data
          }
        },
        { text: '\n\n' },
        { qr: 'https://sivendiweb.com.br/app', fit: '70' },
      ]

      // {text: 'Informações da Consultora(o)',  bold: true,  alignment: 'left'},

      const documentDefinition = { content: contentX };
      pdfMake.createPdf(documentDefinition).open({}, window);

      console.log(documentDefinition)
      console.log(requestPdf)
    }, error => { });



  }


}