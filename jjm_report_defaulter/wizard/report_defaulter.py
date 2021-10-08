# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class ReportDefaulterReportView(models.AbstractModel):
    _name = 'report.jjm_report_defaulter.defaulter_report_template_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        partner_id = data['form']['partner']
        array = []
        args1 = []
        args = []

        if partner_id:
            partner_id = self.env['res.partner'].browse(partner_id) or False
            args.append(('partner_id', '=', int(partner_id.id)))
        else:
            partner_obj = self.env['res.partner'].search([]) or False

        args.append(('state', '=', 'posted'))

        invoice_obj = self.env['account.move'].search(args) or False



        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'partner': partner_id and partner_id.name or ' ',
            'user': self.env.user.name,
        }

        for invoice in invoice_obj:
            if invoice.invoice_date_due:
                if invoice.invoice_date_due < fields.Date.today() and invoice.amount_residual_signed > 0:
                    lineas = {
                        'cliente': invoice.partner_id.name,
                        'telefono': invoice.partner_id.phone or invoice.partner_id.mobile,
                        'calle': invoice.partner_id.street or invoice.partner_id.street or '',
                        'ciudad': invoice.partner_id.city or '',
                        'provincia': invoice.partner_id.state_id.name or '',
                        'pais': invoice.partner_id.country_id.name or '',
                        'horario': invoice.partner_id.contact_time or '',
                        'contrato': invoice.invoice_origin,
                        'canon': invoice.canon,
                        'fecha': invoice.invoice_date.strftime('%d-%m-%Y') or '',
                        'importe': invoice.amount_residual_signed,
                        'currency_id': self.env.company.currency_id,
                        'collector': invoice.collector_id,
                    }
                    array.append(lineas)
        if len(array) < 1 or not invoice_obj:
            raise ValidationError(
                "No se encontraron morosos pendientes!")

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
            'currency_id': self.env.company.currency_id,
        }
