# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ReportCustomerDebtReport(models.AbstractModel):
    # report.nombre modulo.template_id
    _name = 'report.jjm_report_customer_debt.report_customer_debt_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        # LOS DATOS QUE RECIBO DEL WIZARD
        client_id = data['form']['client']
        contract_id = data['form']['contract']

        #DECLARO VARIABLES
        args = []
        args_inv = []
        array = []
        pagadas = 0

        # FILTRO CLIENTE
        if client_id:
            client_obj = self.env['res.partner'].browse(int(client_id)) or False
            args.append(('state', '=', 'confirm'))
            args.append(('partner_id', '=', client_obj.id))

        #FILTRO CONTRATO
        if contract_id:
            args.append(('id', '=', contract_id))
            contract_obj = self.env['contract.contract'].search(args) or False
            args_inv.append(('invoice_origin', '=', contract_obj.name))
        else:
            contract_obj = self.env['contract.contract'].search(args) or False

        # ARMO EL ENCABEZADO
        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'client': client_obj and client_obj.name or False,
            'contract': contract_obj and contract_obj[0].name or False,
            'user': self.env.user.name,
        }
        if not contract_obj:
            raise ValidationError(
                "No se encontraron contratos del Cliente seleccionado!")

        # BUSCO LAS FACTURAS
        for contract in contract_obj:
            invoice_obj = self.env['account.move'].search([
                ('invoice_origin', '=', contract.name),
                ('state', '=', 'posted')], order='canon') or False

            if invoice_obj:
                for invoice in invoice_obj:
                    if invoice.amount_residual > 0:
                        obs = 'Adeuda'
                    else:
                        obs = 'Pagado'
                        pagadas += 1

                    lineas = {
                        'canon': invoice.canon or ' ',
                        'invoice_date': invoice.invoice_date.strftime('%d-%m-%Y') or ' ',
                        'price': invoice.amount_total_signed or 0,
                        'adeuda': invoice.amount_residual or 0,
                        'observation': obs or ' ',
                        'document': invoice.invoice_origin or ' ',
                        'cuotas': contract.cant_cuotas or False or 0,
                        'faltan': contract.cant_cuotas - pagadas or 0,
                        'contract': contract or False,
                    }
                    if lineas:
                        array.append(lineas)
            else:
                raise ValidationError(
                    "No se encontraron Facturas del Cliente seleccionado!")
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }
