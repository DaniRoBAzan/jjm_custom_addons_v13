# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date, datetime, timedelta

class ContractContract(models.Model):
    _inherit = 'contract.contract'

    @api.model
    def default_date(self):
        today = fields.Date.today()
        return today

    date_accession = fields.Date(string='Fecha Adhesión', default=default_date, store=True)
    consultant_id = fields.Many2one('res.partner', "Asesor / Vendedor", store=True)
    campaign_id = fields.Many2one('contract.campaign', string='Campaña', store=True)
    method_payment_id = fields.Many2one('method.paymentjjm', string='Forma de Pago', store=True)
    collector_id = fields.Many2one('res.partner', "Cobrador", store=True)


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('contract.contract') or 'New'
        result = super(ContractContract, self).create(vals)
        return result




