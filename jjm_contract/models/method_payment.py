# -*- codding: utf-8 -*-
from odoo import models, fields


class MethodPayment(models.Model):
    _name = 'method.paymentjjm'
    _description = 'method of payment'

    name = fields.Char(string='Forma de Pago', store=True)