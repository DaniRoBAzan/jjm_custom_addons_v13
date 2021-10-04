# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DustomerDebtReportWizard(models.TransientModel):
    _name = 'customer.debt.report.wizard'

    client = fields.Many2one('res.partner', "Cliente", domain=[("is_customer", "=", True)])
    contract = fields.Many2one('contract.contract', string='Contrato')
    has_parent_contract = fields.Boolean(string='Tener en cuenta contratos dados de baja.', default=False)

    def generate_pdf_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'client': self.client.id,
                'contract': self.contract.id,
                'has_parent_contract': self.has_parent_contract,
            },
        }

        # ref(nombre_modulo.reporte_id)
        print('estoy en el return del wizard!')
        return self.env.ref('jjm_report_customer_debt.customer_debt_report').report_action(self, data=data)

