# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_contract(self):
        self.ensure_one()
        action = self.env.ref('contract.contract_contract_customer_form_view').read()[0]
        ctx = dict(
            default_res_id=self.id,
            default_partner_id=self.partner_id.id,
        )
        return {
            'name': _('Contrato'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'contract.contract',
            'target': 'new',
            'action': action,
            'context': ctx,
        }


