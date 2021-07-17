# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentReportWizard(models.TransientModel):
    _name = 'payment.report.wizard'
    print('entre al wizard class')
    date_start = fields.Date(string='Fecha Inicial', required=True, default=fields.Date.today)
    date_end = fields.Date(string='Fecha Final', required=True, default=fields.Date.today)
    collector = fields.Many2one('res.partner', "Cobrador", domain=[("is_collector", "=", True)])
    print_all = fields.Boolean(string='Imprimir Todos los cobradores')

    #@api.multi
    def generate_pdf_report(self):
        print('entre a la funcion imprimir del wizard')
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
                'collector': self.collector.id,
                'print_all': self.print_all,
            },
        }

        #                      ref `module_name.report_id` as reference.
        print('estoy en el return del wizard!')
        return self.env.ref('jjm_report_payment.payment_report').report_action(self, data=data)

