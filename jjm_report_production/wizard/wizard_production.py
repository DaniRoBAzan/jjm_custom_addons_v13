# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductionReportWizard(models.TransientModel):
    _name = 'production.report.wizard'

    supervisor = fields.Many2one('res.partner', string="Supervisor",  domain="[('is_supervisor', '=', True)]")
    consultant = fields.Many2one('res.partner', string="Asesor / Vendedor",  domain="[('is_consultant', '=', True)]")
    campaign = fields.Many2one('contract.campaign', string='Campaña')

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'supervisor': self.supervisor.id,
                'consultant': self.consultant.id,
                'campaign': self.campaign.id,
            },
        }

        # ref(nombre_modulo.reporte_id)
        return self.env.ref('jjm_report_production.production_report').report_action(self, data=data)

