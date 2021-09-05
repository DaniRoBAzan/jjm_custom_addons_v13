# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime, timedelta


class ContractContract(models.Model):
    _inherit = 'contract.contract'

    parent_contract = fields.Integer('Contrato Padre')

    def get_jjm_last_canon_contract(self):
        #con el name del contrato actual debo buscar las facturas pagadas
        invoice_obj = self.env['account.move'].search([('invoice_origin', '=', self.name),('amount_residual','=',0)])
        if invoice_obj:
            #contarlas y setear a ultimo canon.
            self.jjm_last_canon_contract= len(invoice_obj)
            return len(invoice_obj)
        else:
            return False

    def get_payment_term(self):
        return 9

    def action_create_contract(self):
        action = self.env.ref('contract.contract_contract_customer_form_view').read()[0]
        self.action_cancel()  # cancelamos el contrato actual.
        self.jjm_motivo_baja = "Baja por cambio de plan."
        ctx = dict(
            default_partner_id=self.partner_id.id,
            default_parent_contract=self.id,
            default_campaign_id=self.campaign_id.id,
            default_consultant_id=self.consultant_id.id,
            default_collector_id=self.collector_id.id,
            default_method_payment_id=self.method_payment_id.id,
            #default_payment_term_id=self.get_payment_term(),
            default_jjm_description_moto=self.jjm_description_moto,
            default_jjm_last_canon_contract=self.get_jjm_last_canon_contract(),
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

