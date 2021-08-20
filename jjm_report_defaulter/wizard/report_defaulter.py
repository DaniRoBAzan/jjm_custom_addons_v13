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
        supervisor = data['form']['supervisor']
        partner = data['form']['partner']
        array = []
        encabezado = []
        args1 = []
        args = []
        contador = 0
        importe = 0

        if supervisor:
            supervisor = self.env['res.partner'].browse(int(supervisor))
            args1.append(('jjm_manager', '=', int(supervisor)))
            if partner:
                args1.append(('id', '=', int(partner)))
                partner = self.env['res.partner'].search(args1) or False
                args.append(('partner_id', '=', partner.id))

        else:
            partner = self.env['res.partner'].browse(int(partner))
            args.append(('partner_id', '=', partner.id))


        today = fields.Date.today().strftime('%d-%m-%Y')
        encabezado = {
            'today': today,
            'supervisor': supervisor and supervisor.name,
            'partner': partner and partner.name or '',
            'user': self.env.user.name,
        }

        invoice_obj = self.env['account.move'].search(args) or False
        bandera = True

        for invoice in invoice_obj:
            if invoice.invoice_date_due:
                if invoice.invoice_date_due.day > 15 and invoice.amount_residual_signed > 0:
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
                    bandera = False
        if bandera:
            raise ValidationError(
                "No hay morosos pendientes para el supervisor seleccionado!")


        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': array,
            'encabezado': encabezado,
            'currency_id': self.env.company.currency_id,
        }
