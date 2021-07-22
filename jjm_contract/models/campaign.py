# -*- codding: utf-8 -*-
from odoo import models, fields


class ContractCampaign(models.Model):
    _name = 'contract.campaign'
    _description = 'campaign of the contract'

    name = fields.Char(string='Campaña', store=True)
    date_start = fields.Date(string='Fecha Inicio', store=True)
    date_end = fields.Date(string='Fecha Final', store=True)
    current = fields.Boolean(string='Vigente', store=True)


