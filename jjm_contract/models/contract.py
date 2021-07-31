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
    cant_cuotas = fields.Integer(string='Cantidad Cuotas', default=0, store=True)


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('contract.contract') or 'New'
        result = super(ContractContract, self).create(vals)
        return result

    def _recurring_create_invoice(self):
        res = super(ContractContract, self)._recurring_create_invoice()
        for rec in self:
            res.update({
                'consultant_id': rec.consultant_id.id,
                'campaign_id': rec.campaign_id.id,
                'method_payment_id': rec.method_payment_id.id,
                'collector_id': rec.collector_id.id,
            })
        return res






