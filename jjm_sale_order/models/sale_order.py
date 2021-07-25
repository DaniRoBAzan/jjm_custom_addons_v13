# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    contracts_count = fields.Integer(compute='_compute_contract_count', string='Cant.Contratos', defaul=0)

    def _compute_contract_count(self):
        self.contracts_count = len(self._get_action_contracts_ids())
        return self.contracts_count


    def action_contract(self):
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
        contract_ids = self._get_action_contracts_ids().ids
        action = {
            'res_model': 'contract.contract',
            'type': 'ir.action.act_window',
        }
        if len(contract_ids) == 1:
            action.update({
                'view_mode': 'form',
                'default_res_id': contract_ids[0],
                'default_partner_id': self.partner_id.id,
            })
        else:
            action.update({
                'name': "Contrato",
                'context': [('id', 'in', contract_ids)],
                'view_mode': 'tree,form',
            })
        print(action)
        return action

    def _get_action_contracts_ids(self):
        return self.partner_id.contract_ids
