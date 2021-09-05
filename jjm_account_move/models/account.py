# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = "account.move"

    canon = fields.Integer(string='Canon', default=0, store=True)
    consultant_id = fields.Many2one('res.partner', "Asesor / Vendedor", store=True, readonly=True)
    campaign_id = fields.Many2one('contract.campaign', string='Campaña', store=True, readonly=True)
    method_payment_id = fields.Many2one('method.paymentjjm', string='Forma de Pago', store=True, readonly=True)
    collector_id = fields.Many2one('res.partner', "Cobrador", store=True, readonly=True)


    def action_post(self):
        for rec in self:
            if rec.invoice_origin:
                invoice_obj = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id),
                                                               ('invoice_origin', '=', rec.invoice_origin),
                                                               ('state', '=', 'posted')], order='canon desc',
                                                              limit=1)
                if invoice_obj:
                    contract_obj = self.env['contract.contract'].search([('name', '=',  rec.invoice_origin)])
                    if contract_obj.parent_contract:
                        contract_partner_obj = rec.parent_contract
                        rec.canon = int(contract_partner_obj.canon)
                    else:
                        if rec.partner_id.id and not contract_obj.parent_contract:
                            rec.canon = int(invoice_obj.canon) + 1
                        else:
                            rec.canon = 1
        return super(AccountMove, self).action_post()


    def action_account_invoice_payment_group(self):
        self.ensure_one()
        if self.state != 'posted' or self.invoice_payment_state != 'not_paid':
            raise ValidationError(_('You can only register payment if invoice is posted and unpaid'))
        return {
            'name': _('Register Payment'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.payment.group',
            'view_id': False,
            'target': 'current',
            'type': 'ir.actions.act_window',
            'context': {
                'default_collector_id': self.collector_id.id,
                'default_partner_id': self.partner_id.id,
                'to_pay_move_line_ids': self.open_move_line_ids.ids,
                'pop_up': True,
                'create': True,
                'default_company_id': self.company_id.id,
            },
        }