# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class FleetVehicleModel(models.Model):
    _name = 'jjm_vehicles.vehicle.model'
    _description = 'Model of a vehicle'
    rec_name = 'display_name'
    _order = 'name asc'

    #extiendo el rec_name, para que desde un campo one2many a este modelo, se pueda filtrar por: nombre,marca y cilindrada
    def name_get(self, cr, uid, ids, context=None):
        res = []
        recs = self.browse(cr, uid, ids, context)
        for rec in recs:
            res.append(rec.id, rec.brand_id + rec.name  +  rec.displacement)
        return res

    name = fields.Char('Model name', required=True)
    brand_id = fields.Many2one('jjm_vehicles.vehicle.model.brand', 'Manufacturer', required=True, help='Manufacturer of the vehicle')
    image_128 = fields.Image(related='brand_id.image_128', readonly=False)
    displacement = fields.Char(string="Cilindrada")
    display_name = fields.Char(compute="_compute_new_display_name", store=True, index=True)


    @api.depends('name', 'brand_id')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.brand_id.name:
                name = record.brand_id.name + name
            res.append((record.id, name))
        return res

    @api.depends("name", "brand_id", "displacement")
    def _compute_new_display_name(self):
        for rec in self:
            name = [rec.brand_id.name, rec.name,rec.displacement]
            rec.display_name = name

    def open_pricelist_models(self):
        self.ensure_one()
        action = self.env.ref('jjm_vehicles.jjm_vehicle_price_action').read()[0]
        action.update({
            'view_mode': 'tree,form',
            'domain': [('model_moto', '=', self.id)],
        })
        return action

class FleetVehicleModelBrand(models.Model):
    _name = 'jjm_vehicles.vehicle.model.brand'
    _description = 'Brand of the vehicle'
    _order = 'name asc'

    name = fields.Char('Make', required=True)
    image_128 = fields.Image("Logo", max_width=128, max_height=128)
