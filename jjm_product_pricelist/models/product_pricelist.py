# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from itertools import chain

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_repr
from odoo.tools.misc import get_lang


class Pricelist(models.Model):
    _inherit = "product.pricelist"



class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    price_percent = fields.Float(string='% a imputar')

    @api.onchange('price_percent', 'product_tmpl_id')
    def compute_price_percent(self):
        product_item_obj = self.env['product.pricelist.item'].search([
            ('pricelist_id', '=', self.pricelist_id.id.origin)],
            order="id desc",
            limit=1)
        for rec in self:
            rec.product_tmpl_id = product_item_obj.product_tmpl_id
            rec.min_quantity = product_item_obj.min_quantity
            rec.fixed_price = product_item_obj.fixed_price
            descuento = (rec.price_percent / 100) + 1
            rec.fixed_price = rec.fixed_price * descuento