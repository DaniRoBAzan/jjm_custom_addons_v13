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
        client = data['form']['client']
        contract = data['form']['contract']

        args = []
        array = []
        encabezado = []
        faltan = 0
        pagadas = 0

        # ARMO EL REPORTE
        if client:
            client = self.env['res.partner'].browse(int(client))
            args.append(('partner_id', '=', client.id))
        else:
            raise ValidationError(
                "Debe seleccionar un Cliente para el emitir el reporte!")

        if contract:
            contract = self.env['contract.contract'].browse(int(contract))
            args.append(('invoice_origin', '=', contract.name))


        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'client': client and client.name or '',
            'contract': contract and contract.name or '',
            'user': self.env.user.name,
        }

        invoice_obj = self.env['account.move'].search(args, order='canon') or False
        if invoice_obj is False:
            raise ValidationError(
                "No existe contratos existentes para el cliente seleccionado!")

        for invoice in invoice_obj:
            if invoice.canon != 0:
                if invoice.amount_residual > 0:
                    obs = 'Adeuda'
                else:
                    obs = 'Pagado'
                    pagadas += 1
                contract_obj = self.env['contract.contract'].search([('name', '=', invoice.invoice_origin),
                                                                     ('state', '!=', 'cancel')])
                if contract_obj.parent_contract:#si tiene padre debo traer los datos de la factura del padre
                    contract_obj_parent = self.env['contract.contract'].search([('id', '=', contract_obj.parent_contract),
                                                                         ])

                    for contract in contract_obj:
                        lineas = {
                            'canon': invoice.canon,
                            'invoice_date': invoice.invoice_date.strftime('%d-%m-%Y'),
                            'price': invoice.amount_total_signed,
                            'adeuda': invoice.amount_residual,
                            'observation': obs,
                            'document': invoice.invoice_origin,
                            'cuotas': contract.cant_cuotas or False,
                            'faltan': contract.cant_cuotas - pagadas,
                            'contract': contract,
                        }
                        array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }