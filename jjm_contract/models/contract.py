# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date, datetime, timedelta

class ContractContract(models.Model):
    _inherit = 'contract.contract'

    @api.model
    def default_date(self):
        today = fields.Date.today()
        return today

    date_accession = fields.Date(string='Fecha Adhesión', default=default_date)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('contract.contract') or 'New'
        result = super(ContractContract, self).create(vals)
        return result




