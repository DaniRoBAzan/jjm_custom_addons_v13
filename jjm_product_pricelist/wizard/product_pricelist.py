# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class PricelistWizard(models.Model):
    _name = "product.pricelist.wizard"

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    product_pricelist_id = fields.Many2one('product.pricelist', string='Moto')
    #product_id = fields.Many2one(related='product_pricelist_id.product_id', string='Producto')
    related_fixed_price = fields.Float(related='product_pricelist_id.item_ids.fixed_price',
                               string='Precio Anterior', default=0)
    related_date_start = fields.Date(related='product_pricelist_id.item_ids.date_start',
                               string='Fecha Inicio Anterior')
    related_date_end = fields.Date(related='product_pricelist_id.item_ids.date_end',
                               string='Fecha Final Anterior')

    name = fields.Char('Nombre de la tarifa', required=True, translate=True)
    price_percent = fields.Float(string='% a imputar')
    fixed_price = fields.Float(string='Precio Actualizado')
    date_start = fields.Date(string="Nueva Fecha Inicio")
    date_end = fields.Date(string="Nueva Fecha Final")
    currency_id = fields.Many2one('res.currency', 'Currency', default=_get_default_currency_id, required=True)


    @api.onchange("price_percent")
    def _onchange_percentaje_price(self):
        for rec in self:
            if self.product_pricelist_id:
                descuento = (rec.price_percent / 100) + 1
                rec.fixed_price = rec.related_fixed_price * descuento


    @api.model
    def create(self, vals_list):
        #product_obj = self.env['product.product'].search(['id', '=', vals_list.get('product_pricelist_id')])
        #pricelist_obj = self.env['product.pricelist.item'].search([('product_id', '=', vals_list.get('product_id', False))])
        # pricelist_obj = self.env['product.pricelist.item']
        # pricelist_obj.create({
        #     'name': vals_list.get('name', False),
        #     'currency_id': vals_list.get('currency_id', False),
        #     'product_templ_id': vals_list.get('product_pricelist_id', False),
        #     'fixed_price': vals_list.get('fixed_price', False),
        #     'date_start': vals_list.get('date_start', False),
        #     'date_end': vals_list.get('date_end', False),
        # })
        print('vals_list=', vals_list)
        #print('pricelist_obj=', pricelist_obj)



