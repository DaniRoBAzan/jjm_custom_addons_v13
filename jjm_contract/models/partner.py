# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'


    paid_state = fields.Char(string='Estado de Deuda', required=True, compute='_compute_paid_state', readonly=True ,default='no declarado')
    paid_state_search = fields.Char(string='Estado Deuda Search', default='no declarado')

    def _compute_paid_state(self):
        for rec in self:
            if rec.customer:
                if rec.debt_balance <= 0:
                    rec.paid_state = 'Al día'
                    rec.paid_state_search = rec.paid_state
                else:
                    rec.paid_state = 'Adeuda'
                    rec.paid_state_search = rec.paid_state


