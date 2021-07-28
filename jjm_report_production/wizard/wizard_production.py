# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductionReportWizard(models.TransientModel):
    _name = 'production.report.wizard'

    consultant = fields.Many2one('res.partner', string="Asesor / Vendedor",  domain="[('is_consultant', '=', True)]")
    campaign = fields.Many2one('contract.campaign', string='Campaña')
    #print_all = fields.Boolean(string='Imprimir Todos.')

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'consultant': self.consultant.id,
                'campaign': self.campaign.id,
                #'print_all': self.print_all,
            },
        }

        # ref(nombre_modulo.reporte_id)
        return self.env.ref('jjm_report_production.production_report').report_action(self, data=data)

