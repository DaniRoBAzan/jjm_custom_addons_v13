# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ReportPaymentCollectorReport(models.AbstractModel):
    # report.nombre modulo.template_id
    _name = 'report.jjm_report_payment.report_payment_collector_pdf'

    def get_direction_partner(self, partner):
        direction = ''
        direction += partner.street and partner.street or ''
        direction += partner.street2 and ' - ' + partner.street2 or ''
        direction += partner.zip and ' C.Postal: ' + partner.zip or ''
        direction += partner.city and ' ' + partner.city or ''
        direction += partner.state_id and ' ' + partner.state_id.name or ''
        return direction
    
    @api.model
    def _get_report_values(self, docids, data=None):
        # LOS DATOS QUE RECIBO DEL WIZARD
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        collector = data['form']['collector']
        array = []
        encabezado = []
        contrato = ''
        canon = ''
    # ARMO EL REPORTE
        if date_start and date_end:
            args = [('payment_date',
                        '>=', datetime.strptime(date_start, '%d-%m-%Y')),
                    ('payment_date',
                        '<=', datetime.strptime(date_end, '%d-%m-%Y')),
                    ]
            if collector:
                collector = self.env['res.partner'].browse(int(collector))
                collector_in_contract = self.env['contract.contract'].search([('collector_id', '=', collector.id)])
                if collector_in_contract:
                    args.append(('collector_id', '=', collector.id))
                else:
                    raise ValidationError(
                        "No existen contratos de este cobrador!")
            else:
                collector = self.env['res.partner']
            payment_obj = self.env['account.payment.group'].search(args, order='partner_id desc') or False
            today = fields.Date.today()
            encabezado = {
                'today': today.strftime('%d-%m-%Y'),
                'date_start': date_start,
                'date_end': date_end,
                'collector': collector and collector.name or '',
                'user': self.env.user.name,
            }
            if payment_obj is False:
                raise ValidationError(
                    "No hay pagos asignados en el rango de fechas seleccionado!")

            for payment in payment_obj:
                for p in payment.matched_move_line_ids:
                    contrato = p.move_id.invoice_origin
                    canon = p.move_id.canon
                lineas = {
                    'cliente': payment.partner_id and payment.partner_id.name or ' ',
                    'direccion': self.get_direction_partner(payment.partner_id) or ' ',
                    'telefono': payment.partner_id.phone or payment.partner_id.mobile or ' ',
                    'contrato': contrato or ' ',
                    'canon': canon or ' ',
                    'fecha': payment.payment_date and payment.payment_date.strftime('%d-%m-%Y') or ' ',
                    'importe': payment.payments_amount or 0,
                    'collector': payment.collector_id or collector,
                }
                array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }
