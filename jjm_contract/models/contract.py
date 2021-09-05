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
    cant_cuotas = fields.Integer(string='Cantidad Cuotas', default=0, store=True, help='Escribir la cantidad de cuotas que debera abonar el cliente, para este contrato.')

    jjm_motivo_baja = fields.Char(string='Motivo de Baja')
    jjm_contract_state = fields.Char(string='Estado',
                                     default="Borrador",
                                     compute='_compute_state',
                                     store=True,
                                     readonly=True)
    jjm_date_unsubscribe = fields.Date(string='Fecha Baja',
                                       default=False,
                                       compute='_compute_jjm_date_unsubscribe',
                                       store=True,
                                       readonly=True)
    jjm_description_moto = fields.Text(string='Moto', store=True)
    jjm_last_canon_contract = fields.Integer(string='Ultimo canon', readonly=True, default=0)

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
                # 'canon': rec.get_canon(),
            })
        return res

    # def get_canon(self):
    #     for rec in self:
    #         if rec.invoice_origin:
    #             invoice_obj = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id),
    #                                                            ('invoice_origin', '=', rec.invoice_origin),
    #                                                            ('state', '=', 'posted')], order='canon desc',
    #                                                           limit=1)
    #             if invoice_obj:
    #                 if rec.parent_id:
    #                     contract_partner_obj = rec.parent_id
    #                     rec.canon = int(contract_partner_obj.canon)
    #                 else:
    #                     if rec.partner_id and not rec.parent_id:
    #                         rec.canon = int(invoice_obj.canon) + 1
    #                     else:
    #                         rec.canon = 1
    #     return rec.canon

    @api.depends('state')
    def _compute_state(self):
        for rec in self:
            if rec.state == 'draft':
                rec.jjm_contract_state = 'Borrador'
            if rec.state == 'confirm':
                rec.jjm_contract_state = 'Iniciado'
            if rec.state == 'cancel':
                rec.jjm_contract_state = 'Baja'

    @api.depends('state')
    def _compute_jjm_date_unsubscribe(self):
        for rec in self:
            if rec.state == 'cancel':
                rec.jjm_date_unsubscribe = fields.Date.today()
            else:
                rec.jjm_date_unsubscribe = False
