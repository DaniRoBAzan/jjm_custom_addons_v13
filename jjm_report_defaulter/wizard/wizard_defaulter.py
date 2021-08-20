# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DefaulterReportWizard(models.TransientModel):
    _name = 'defaulter.report.wizard'

    supervisor = fields.Many2one('res.partner', string="Supervisor",  domain="[('is_supervisor', '=', True)]")
    partner = fields.Many2one('res.partner', string="Cliente",  domain="[('is_customer', '=', True)]")


    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'supervisor': self.supervisor.id,
                'partner': self.partner.id,
            },
        }

        return self.env.ref('jjm_report_defaulter.defaulter_report').report_action(self, data=data)

