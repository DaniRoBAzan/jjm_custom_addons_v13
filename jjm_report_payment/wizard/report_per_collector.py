# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ReportPaymentCollectorReport(models.AbstractModel):
    # report.nombre modulo.template_id
    _name = 'report.jjm_report_payment.report_payment_collector_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        # LOS DATOS QUE RECIBO DEL WIZARD
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        collector = data['form']['collector']
        array = []
        encabezado = []

    # ARMO EL REPORTE
        if date_start and date_end:
            args = [('payment_date',
                        '>=', datetime.strptime(date_start, '%d-%m-%Y')),
                    ('payment_date',
                        '<=', datetime.strptime(date_end, '%d-%m-%Y')),
                    ]
            if collector:
                collector = self.env['res.partner'].browse(int(collector))
                args.append(('collector_id', '=', collector.id))

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
                lineas = {
                    'cliente': payment.partner_id and payment.partner_id.name or ' ',
                    'telefono': payment.partner_id.phone or payment.partner_id.mobile or ' ',
                    'contrato': payment.matched_move_line_ids[0] and payment.matched_move_line_ids[0].move_id.invoice_origin or ' ',
                    'canon': payment.matched_move_line_ids[0] and payment.matched_move_line_ids[0].move_id.canon or ' ',
                    'fecha': payment.payment_date and payment.payment_date.strftime('%d-%m-%Y') or ' ',
                    'importe': payment.payments_amount or ' ',
                    'collector': payment.collector_id or False,
                }
                array.append(lineas)

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'encabezado': encabezado,
            'docs': array,
            'currency_id': self.env.company.currency_id,
        }
