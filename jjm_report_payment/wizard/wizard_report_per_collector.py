# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentReportWizard(models.TransientModel):
    _name = 'payment.report.wizard'

    date_start = fields.Date(string='Fecha Inicial', required=True, default=fields.Date.today)
    date_end = fields.Date(string='Fecha Final', required=True, default=fields.Date.today)
    collector = fields.Many2one('res.partner', "Cobrador", domain=[("is_collector", "=", True)])

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'date_start': self.date_start.strftime('%d-%m-%Y'),
                'date_end': self.date_end.strftime('%d-%m-%Y'),
                'collector': self.collector.id,
            },
        }

        # ref(nombre_modulo.reporte_id)
        print('estoy en el return del wizard!')
        return self.env.ref('jjm_report_payment.payment_collector_report').report_action(self, data=data)

