# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    paid_state = fields.Char(
        string='Estado de Deuda',
        compute='_compute_paid_state',
        readonly=True,
        store=True
    )

    def _compute_debt_balance(self):
        for rec in self:
            debt_balance = rec.credit - rec.debit
            if rec.is_customer:
                if debt_balance <= 0:
                    rec.paid_state = 'Al día'
                else:
                    rec.paid_state = 'Adeuda'
            else:
                rec.paid_state = 'No es cliente'
        return super(ResPartner, self)._compute_debt_balance()

