# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class ReportPaymentReportView(models.AbstractModel):
    _name = 'paymentreport.payment_report_template_pdf'
    print('entre al reporte class')

    @api.model
    def _get_report_values(self, docids, data=None):
        print("entre a la funcion del reporte!")
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        collector = data['form']['collector']
        print_all = data['form']['print_all']
        print('recibi: date_start: ', date_start, '/ date_end: ', date_end, ' / collector: ',collector, ' / print_all: ',print_all)

        # date_start = datetime.strptime(date_start, DATE_FORMAT)
        # date_end = datetime.strptime(date_end, DATE_FORMAT)
        # delta = timedelta(days=1)
        # date = start_date
        #     start_date += delta

        list_partner = []
        list_invoices = []
        docs = []
        total = 0
        while date_start <= date_end:
            # SI EL CHECK ES FALSO
            if print_all is False:
    # SI NO ESTA TILDADO PRINT_ALL DEBO BUSCAR EN LOS CONTRATOS TODOS LOS CLIENTES QUE TENGAN DE COBRADOR
    # AL COBRADOR ELEGIDO EN EL WIZARD Y CARGARLOS EN UNA LISTA, O BIEN TRAER TODOS.
                contract_obj = self.env['contract.contract'].search(['collector', '=', collector])
            else:
                contract_obj = self.env['contract.contract']

            for partner in contract_obj:
                print('--> partner del contract: ', partner)
                list_partner.append(partner)
    # LUEGO DEBO BUSCAR EN LAS FACTURAS TODOS ESOS CLIENTES Y TRAER LAS FACTURAS
    # FILTRADAS POR LAS FECHAS  ELEGIDAS EN EL WIZARD.
                account_obj = self.env['account.move']
                for invoice in account_obj:
                    print('--> invoice del account: ', invoice)
                    if invoice.partner_id in list_partner:
                        if (invoice.invoice_date >= date_start) and (invoice.invoice_date <= date_end) and \
                                (invoice.type == 'invoice'):
                            # ARMAMOS UNA LISTA CON LOS CLIENTES ENCONTRADOS
                            list_invoices.append(invoice.id)
                            # TRAER ULTIMA FACTURA DEL CLIENTE ENCONTRADO
                            for item in list_invoices:
                                invoice_obj = self.env['account.move'].search([('id', 'in', list_invoices[item])],
                                                                              order="invoice_date desc", limit=1)
                                partner_obj = self.env['res.partner'].search(invoice_obj.res_partner)
                                total += invoice_obj.amount_total_signed
                                docs.append({
                                    'contrato': invoice_obj.invoice_origin,
                                    'cliente': partner_obj.name,
                                    'dni': partner_obj.vat,
                                    'canon': invoice_obj.canon,
                                    'importe': invoice_obj.amount_total_signed,
                                })
                                print('docs: ',docs)
                            docs.append({'total': total})
        print('docs=', docs)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
