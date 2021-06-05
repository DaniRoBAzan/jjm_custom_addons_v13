# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class FleetVehicleModel(models.Model):
    _name = 'jjm_vehicles.vehicle.model'
    _description = 'Model of a vehicle'
    rec_name = 'name'
    _order = 'name asc'

    #extiendo el rec_name, para que desde un campo one2many a este modelo, se pueda filtrar por: nombre,marca y cilindrada
    def name_get(self, cr, uid, ids, context=None):
        res = []
        recs = self.browse(cr, uid, ids, context)
        for rec in recs:
            res.append((rec.id, rec.name + ' ' + rec.brand_id  + ' ' + rec.displacement))
        return res

    name = fields.Char('Model name', required=True)
    brand_id = fields.Many2one('jjm_vehicles.vehicle.model.brand', 'Manufacturer', required=True, help='Manufacturer of the vehicle')
    #vendors = fields.Many2many('res.partner', 'jjm_vehicle_model_vendors', 'model_id', 'partner_id', string='Vendors')
    #manager_id = fields.Many2one('res.users', 'Fleet Manager')
    # manager_id = fields.Many2one('res.users', 'Fleet Manager', default=lambda self: self.env.uid,
    #                              domain=lambda self: [('groups_id', 'in', self.env.ref('jjm_vehicles.fleet_group_manager').id)])
    image_128 = fields.Image(related='brand_id.image_128', readonly=False)
    displacement = fields.Char(string="Cilindrada")



    @api.depends('name', 'brand_id')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if record.brand_id.name:
                name = record.brand_id.name + '/' + name
            res.append((record.id, name))
        return res

    def open_pricelist_models(self):
        print("==> boton que abre lista de precios!")
        self.ensure_one()
        #purchase_requisition_ids = self._get_action_view_pr_ids().ids
        action_view_prif = self.env.ref('jjm_vehicle_price_action').read()[0]
        action_view_prif.update({
            'name': ("Price List of vehicle"),
            # 'name': _("Price List of vehicle: %s", self.name),
            'domain': [('id', 'in', self.id)],
            'view_mode': 'tree,form',
        })
        print("return..")
        return action_view_prif


class FleetVehicleModelBrand(models.Model):
    _name = 'jjm_vehicles.vehicle.model.brand'
    _description = 'Brand of the vehicle'
    _order = 'name asc'

    name = fields.Char('Make', required=True)
    image_128 = fields.Image("Logo", max_width=128, max_height=128)
