# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class EmissionReport(models.AbstractModel):
    # report.nombre modulo.template_id
    _name = 'report.jjm_report_emission.jjm_emission_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # LOS DATOS QUE RECIBO DEL WIZARD
        month = data['form']['month']
        month = int(month)
        collector = data['form']['collector']
        array = []
        args = []
        encabezado = []

    # ARMO EL REPORTE
        if collector:
            collector = self.env['res.partner'].browse(int(collector))
            args.append(('collector_id', '=', collector.id))
        # if month:
        args.append(('invoice_date', '!=', False))
        args.append(('state', '=', 'posted'))

        today = fields.Date.today()
        encabezado = {
            'today': today.strftime('%d-%m-%Y'),
            'month': month,
            'collector': collector and collector.name or '',
            'user': self.env.user.name,
        }

        invoice_obj = self.env['account.move'].search(args) or False
        bandera = True

        for invoice in invoice_obj:
            contract_obj = self.env['contract.contract'].search([('name', '=', invoice.invoice_origin)])
            if contract_obj.state != 'cancel':
                if invoice.invoice_date.month == month:
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
                        'importe': invoice.amount_total_signed,
                        'currency_id': self.env.company.currency_id,
                        'collector': invoice.collector_id,
                    }
                    array.append(lineas)
                    bandera = False
        if bandera:
            raise ValidationError(
                    "No hay facturas emitidas de este Cobrador en el mes seleccionado!")

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }
