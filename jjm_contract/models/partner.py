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

    @api.depends('debt_balance', 'is_customer')
    def _compute_paid_state(self):
        for rec in self:
            if rec.is_customer:
                if rec.debt_balance <= 0:
                    rec.paid_state = 'Al día'
                else:
                    rec.paid_state = 'Adeuda'
            else:
                rec.paid_state = 'No es cliente'

