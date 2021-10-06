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
        has_parent_contract = data['form']['has_parent_contract']

        #DECLARO VARIABLES
        args = []
        args_inv = []
        parent_args = []
        array = []
        encabezado = []
        faltan = 0
        pagadas = 0

        # FILTRO CLIENTE
        if client_id:
            client_obj = self.env['res.partner'].browse(int(client_id)) or False

        # FILTRO TRAER TODOS LOS CONTRATOS
        if has_parent_contract:
            args.append(('state', '!=', 'draft'))
            args.append(('partner_id', '=', client_obj.id))
        else:
            args.append(('state', '=', 'confirm'))
            args.append(('partner_id', '=', client_obj.id))

        #FILTRO CONTRATO
        if contract_id:
            args.append(('id', '=', contract_id))
            # FILTRO TRAER TODOS LOS CONTRATOS
            if has_parent_contract:
                args.append(('parent_contract', '=', contract_id))
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
            invoice_obj = self.env['account.move'].search([('invoice_origin', '=', contract.name)],
                                                          order='canon') or False

            for invoice in invoice_obj:
                if invoice.amount_residual > 0:
                    obs = 'Adeuda'
                else:
                    obs = 'Pagado'
                    pagadas += 1

                # if contract.state == 'confirm':
                #     estado = 'Activo'
                # else:
                #     estado = 'Dado de baja'

                lineas = {
                    'canon': invoice.canon,
                    'invoice_date': invoice.invoice_date.strftime('%d-%m-%Y'),
                    'price': invoice.amount_total_signed,
                    'adeuda': invoice.amount_residual,
                    'observation': obs,
                    'document': invoice.invoice_origin,
                    'cuotas': contract.cant_cuotas or False,
                    'faltan': contract.cant_cuotas - pagadas,
                    'contract': contract or False,
                    # 'state': estado,
                }
                array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }
