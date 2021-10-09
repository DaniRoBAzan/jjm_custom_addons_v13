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
        for rec in self:# si la factura a publicar tiene referencia a contrato
            if rec.invoice_origin:# busco el contrato relacionado
                contract_obj = self.env['contract.contract'].search([('name', '=', rec.invoice_origin)])
                if contract_obj.jjm_last_canon_contract:# si el contrato tiene ultimo canon sesteo el canon
                    contract_obj.jjm_last_canon_contract += 1
                else:# si no tiene ultimo canon
                    contract_obj.jjm_last_canon_contract = 1
                rec.canon = contract_obj.jjm_last_canon_contract# seteo campo canon de factura actual
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

    class ValidateAccountMove(models.TransientModel):
        _inherit = "validate.account.move"

        def validate_move(self):
            if self._context.get('active_model') == 'account.move':
                invoice_obj = self.env['account.move'].browse(self.env.context.get('active_ids'))
                for rec in invoice_obj:  # si la factura a publicar tiene referencia a contrato
                    if rec.invoice_origin:  # busco el contrato relacionado
                        contract_obj = self.env['contract.contract'].search([('name', '=', rec.invoice_origin)])
                        if contract_obj.jjm_last_canon_contract:  # si el contrato tiene ultimo canon sesteo el canon
                            contract_obj.jjm_last_canon_contract += 1
                        else:  # si no tiene ultimo canon
                            contract_obj.jjm_last_canon_contract = 1
                        rec.canon = contract_obj.jjm_last_canon_contract  # seteo campo canon de factura actual
            return super().validate_move()
