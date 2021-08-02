# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    is_kit = fields.Boolean(string="Es un Kit", default=False, store=True)
    model_moto = fields.Many2one('jjm_vehicles.vehicle.model', string="Modelo elegido", store=True)
    displacement = fields.Char(string="Cilindradas", related='model_moto.displacement')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    model_moto = fields.Char(related='product_tmpl_id.model_moto.display_name', string="Modelo elegido")

