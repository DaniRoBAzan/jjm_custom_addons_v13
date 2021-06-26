# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class VehiclesPrice(models.Model):
    _name = 'jjm_vehicles.vehicles_price'
    _description = 'Model of vehicles price to vehicles'
    _order = 'name asc'

    def _get_default_currency_id(self):
        return self.env.company.currency_id.id

    name = fields.Char('Nombre Tarifa', required=True)
    currency_id = fields.Many2one('res.currency', 'Currency', default=_get_default_currency_id, required=True)
    model_moto = fields.Many2one('jjm_vehicles.vehicle.model', string="Modelo de la moto", store=True)
    fixed_price_moto = fields.Float('Precio',digits='Product Price')
    date_start_moto = fields.Date('Fecha inicial')
    date_end_moto = fields.Date('Fecha final')
