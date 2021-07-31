# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    canon = fields.Integer(string='Canon', default=0, store=True)
    consultant_id = fields.Many2one('res.partner', "Asesor / Vendedor", store=True, readonly=True)
    campaign_id = fields.Many2one('contract.campaign', string='Campaña', store=True, readonly=True)
    method_payment_id = fields.Many2one('method.paymentjjm', string='Forma de Pago', store=True, readonly=True)
    collector_id = fields.Many2one('res.partner', "Cobrador", store=True, readonly=True)

    @api.model
    def action_post(self):
        for rec in self:
            if rec.invoice_origin:
                if rec.partner_id:
                    invoice_obj = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id),
                                                                   ('invoice_origin', '=', rec.invoice_origin),
                                                                   ('state', '=', 'posted')], order='canon desc', limit=1)
                    if invoice_obj:
                        rec.canon = int(invoice_obj.canon) + 1
                    else:
                        rec.canon = 1
        return super(AccountMove, self).action_post()
