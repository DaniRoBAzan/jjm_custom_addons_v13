# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UnsubscribeReportWizard(models.TransientModel):
    _name = 'unsubscribe.report.wizard'

    supervisor = fields.Many2one('res.partner', string="Supervisor",  domain="[('is_supervisor', '=', True)]")
    consultant = fields.Many2one('res.partner', string="Asesor / Vendedor",  domain="[('is_consultant', '=', True)]")
    campaign = fields.Many2one('contract.campaign', string='Campaña', required=True)
    date_start = fields.Date(string='Fecha Inicial', default=fields.Date.today, required=True)
    date_end = fields.Date(string='Fecha Final', default=fields.Date.today, required=True)

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'supervisor': self.supervisor.id,
                'consultant': self.consultant.id,
                'campaign': self.campaign.id,
                'date_start': self.date_start.strftime('%d-%m-%Y'),
                'date_end': self.date_end.strftime('%d-%m-%Y'),
            },
        }

        return self.env.ref('jjm_report_unsubscribe.unsubscribe_report').report_action(self, data=data)

