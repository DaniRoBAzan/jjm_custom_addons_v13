# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api


class ReportPaymentCollectorReport(models.AbstractModel):
    #report.nombre modulo.template_id
    _name = 'report.jjm_report_payment.payment_report_collector_template_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
    # LOS DATOS QUE RECIBO DEL WIZARD
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        collector = data['form']['collector']
        array = []

    # ARMO EL REPORTE
        if date_start <= date_end:
            collector = self.env['res.partner'].browse(int(collector))
            payment_obj = self.env['account.payment.group'].search([('collector_id', '=', collector.id),
                                                                    ('payment_date', '>=', date_start),
                                                                    ('payment_date', '<=', date_end),
                                                                    ], order='partner_id desc') or False
            for payment in payment_obj:
                lineas = {
                    'cliente': payment.partner_id.name,
                    'dni': payment.partner_id.vat,
                    'contrato': payment.to_pay_move_line_ids.move_id.invoice_origin,
                    'canon': payment.to_pay_move_line_ids.move_id.canon,
                    'fecha': payment.payment_date,
                    'importe': payment.payments_amount,
                }
                array.append(lineas)


        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': array,
        }
