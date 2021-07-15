# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    canon = fields.Integer(string='Canon', store=True)

    def action_post(self):
        for rec in self:
            if rec.partner_id:
                invoice_obj = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id),
                                                               ('invoice_origin', '=', rec.invoice_origin),
                                                               ('state', '=', 'posted')])
                if invoice_obj:
                    rec.canon = len(invoice_obj) + 1
                else:
                    pass
        return super(AccountMove, self).action_post()




