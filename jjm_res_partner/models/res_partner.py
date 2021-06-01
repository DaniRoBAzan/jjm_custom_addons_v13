# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    #PARTNER
    marital = fields.Selection(
        string='Estado Civil',
        selection=
        [('single', 'Soltero/a'),
         ('married', 'Casado/a'),
         ('divorced', 'Divorciado/a'),
         ('widower', 'Viudo/a')],
        default='single'
    )
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')
    contact_time = fields.Char(string='Hora de contacto')
    enterprice_name = fields.Char(string='Empresa', help='Escribe aqui el nombre de la Empresa del cliente')
    enterprice_address = fields.Char(string='Direccion Empresa' ,help='Escribe aqui el nombre de la direccion de la Empresa del cliente')

    is_partner = fields.Boolean(string= 'Es Socio', store=True)
    is_collector = fields.Boolean(string= 'Es Cobrador', store=True)
    is_consultant = fields.Boolean(string= 'Es Asesor', store=True)
