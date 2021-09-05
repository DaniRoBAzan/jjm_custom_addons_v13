# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime, timedelta


class ContractContract(models.Model):
    _inherit = 'contract.contract'

    parent_contract = fields.Integer('Contrato Padre')

    def action_create_contract(self):
        action = self.env.ref('contract.contract_contract_customer_form_view').read()[0]
        self.action_cancel()  # cancelamos el contrato actual.
        ctx = dict(
            default_partner_id=self.partner_id.id,
            default_parent_contract=self.id,
            default_campaign_id=self.campaign_id.id,
            default_consultant_id=self.consultant_id.id,
            default_collector_id=self.collector_id.id,
            default_method_payment_id=self.method_payment_id.id,
            default_jjm_description_moto=self.jjm_description_moto,
            default_jjm_last_canon_contract=self.jjm_last_canon_contract,
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

