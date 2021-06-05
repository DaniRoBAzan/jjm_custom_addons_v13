# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    initial_canon = fields.Float(string="Canon Inicial", store=True)
    is_kit = fields.Boolean(string="Es un Kit", default=False, store=True)
    #este debe ir debajo de sale_ok y estar invisible, a no ser que este cambie a true.
    model_moto = fields.Many2one('jjm_vehicles.vehicle.model', string="Modelo de la moto", store=True)
    displacement = fields.Char(string="Cilindradas", related='model_moto.displacement')

