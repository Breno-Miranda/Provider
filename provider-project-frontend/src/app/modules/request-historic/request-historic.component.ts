import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import pdfMake from 'pdfmake/build/pdfmake';
import pdfFonts from 'pdfmake/build/vfs_fonts';
pdfMake.vfs = pdfFonts.pdfMake.vfs;


// service 
import { RequestService } from 'src/app/core/services/requets.service';
import { first } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-request-historic',
  templateUrl: './request-historic.component.html',
  styleUrls: ['./request-historic.component.scss']
})
export class RequestHistoricComponent implements OnInit {

  // array select 
  lots: Array<[]> = [];
  campaigns: Array<[]> = [];
  catalogs: Array<[]> = [];
  users: Array<[]> = [];

  // form
  formFilter: FormGroup;

  // array table 
  requests: Array<[]> = [];

  // pagination 
  itemsPerPage: number = 0;
  totalItems: any = 0;
  page: any = 1;
  previousPage: any;

  constructor(
    private requestService: RequestService,
    private formBuilder: FormBuilder,
    private toastr: ToastrService,
  ) {
    this.formFilter = this.formBuilder.group({
      catalog: ['', Validators.required],
      campaign: ['', Validators.required],
      lot: ['', Validators.required],
      profile: ['', Validators.required],
    });
  }

  ngOnInit() {

    // Carregar os selects 
    this.requestService.getRequest({
      type_code: 4,
    }).pipe(first()).subscribe(data => {
      this.lots = data['lots']
      this.campaigns = data['campaigns']
      this.catalogs = data['catalogs']
      this.users = data['users']
    }, error => {
      // informa uma mensagem de erro caso aconteca
    });

    this.requestService.getAll({
      pagination: true,
    }).subscribe( data => {
      this.requests = data['results'];
      this.totalItems = data['count'];
      this.itemsPerPage = data['limit'];
    }, error => {
      // informa uma mensagem de erro caso aconteca
    });
  }

  // get form

  get f() {
    return this.formFilter.controls;
  }

  // pagination
  
  loadPage(page: number) {
    if (page !== this.previousPage) {
      this.previousPage = page;
      this.loadData(page);
    }
  }

  loadData(page) {
    this.requestService.getAll({
      pagination: true,
      page: page
    }).subscribe( data => {
      this.requests = data['results'];
      this.page = page 
      this.itemsPerPage = data['limit'];
    }, error => {
      // informa uma mensagem de erro caso aconteca
    });
  }

  generatePdf(request_id) {

    this.toastr.success("Aguarde..PDF está sendo inicializado!");

    var requestPdf = [];

    this.requestService.getPrintPdf({
      'request_id': request_id
    }).subscribe(requests => {
      
      requestPdf = requests;

      var data = [];
      var desconto = 0;
      var valor = 0;

      requestPdf['itens'].forEach((value, index) => {

        data[0] = [
          { text: 'Codigo', bold: true },
          { text: 'Tm', bold: true },
          { text: 'Descricao', bold: true },
          { text: 'Pag', bold: true },
          { text: 'Qt', bold: true },
          { text: 'Unitario', bold: true },
          { text: 'Total', bold: true },
          { text: 'Ganho', bold: true },
          { text: 'Liquido', bold: true }];

        data[index + 1] = [ 
          { text: value['_product']['reference'] },
          { text: value['_product']['size'] },
          { text: value['_product']['description'] },
          { text: value['_product']['page'] },
          { text: value['amount'] },
          { text: value['_product']['sale_price'] },
          { text: value['total'] },
          { text: value['amount'] * value['_product']['value_provider'] },
          { text: (value['total'] - (value['amount'] * value['_product']['value_provider'])).toFixed(2) },
        ];

          desconto += (value['amount'] * value['_product']['value_provider']);
          valor += value['total'] - (value['amount'] * value['_product']['value_provider']);
      });

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
                'Pedido:' + '  ' + requestPdf['id'],
                'Catalogo: ' + '  ' + requestPdf['_catalog']['_catalog']['name'],
                'Revista:' + '  ' + requestPdf['_catalog']['reference'],
                'Valor:' + '  ' + requestPdf['amount'],
                'Data:' + '  ' + requestPdf['create_date'],
              ]
            }
          ]
        },
        { text: '\n\nTabela de Itens:\n\n', fontSize: 14, bold: true },
        {
          style: 'tableExample',
          table: {
            fontSize: 8,
            headerRows: 1,
            widths: ['auto', 'auto', 'auto', 'auto', 'auto', 'auto', 'auto', 'auto', 'auto'],
            body: data
          }
        },
        { text: '\n\nTotal do Pedido:' + '  R$ ' + requestPdf['amount'] +'', fontSize: 14, bold: true, alignment: 'center' },
        { text: 'Desconto:' + '  R$ ' + (desconto).toFixed(2) + '\n\n', fontSize: 14, bold: true, alignment: 'center' },
        { text: 'Valor à Pagar:' + '  R$ ' + (valor).toFixed(2) + '\n\n', fontSize: 14, bold: true, alignment: 'center' },
        { text: '\n\n' },
        { qr: 'https://sivendiweb.com.br/app', fit: '70' },
      ]

      const documentDefinition = { content: contentX };
      pdfMake.createPdf(documentDefinition).open({}, window);

    }, error => {
      // informar um error se case houver.
    });

  }
}