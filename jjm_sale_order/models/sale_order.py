# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    contracts_count = fields.Integer(compute='_compute_contract_count', string='Cant.Contratos', defaul=0)

    def _compute_contract_count(self):
        self.contracts_count = len(self._get_action_contracts_ids())
        return self.contracts_count


    def action_create_contract(self):
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

    def action_contracts_ids(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Contratos"),
            "res_model": "contract.contract",
            "domain": [('id', 'in', self._get_action_contracts_ids().ids)],
            "view_mode": "tree,form",
            "context": self.env.context,
        }

    def _get_action_contracts_ids(self):
        return self.partner_id.contract_ids
