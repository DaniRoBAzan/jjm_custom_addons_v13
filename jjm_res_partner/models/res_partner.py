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
         ('widower', 'Viudo/a'),
         ('concubine', 'Concubino/a')],
        default='single'
    )
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')
    contact_time = fields.Char(string='Hora de contacto')

    #ENTERPRISE
    enterprise_name = fields.Char(string='Nombre', help='Escribe aqui el nombre de la Empresa del cliente.')
    enterprise_address = fields.Char(string='Direccion' ,help='Escribe aqui la direccion de la Empresa del cliente.')
    enterprise_zip = fields.Char(string='Codigo Postal', help='Escribe aqui el codigo postal de la Empresa del cliente.')
    enterprise_city = fields.Char(string='Ciudad', help='Escribe aqui el nombre de la ciudad de la Empresa del cliente.')
    enterprise_state = fields.Char(string='Provincia', help='Escribe aqui el nombre de la Provincia de la Empresa del cliente.')
    enterprise_country = fields.Char(string='Pais', help='Escribe aqui el nombre del pais de la Empresa del cliente.')


    is_associated = fields.Boolean(string='Es Socio', store=True)
    is_supervisor = fields.Boolean(string='Es Supervisor', store=True)
    is_consultant = fields.Boolean(string='Es Asesor / Vendedor', store=True, domain={'invisible': [('is_supplier','=',False)]})
    code_consultant = fields.Char(Strin='Codigo Asesor', store=True)
    is_collector = fields.Boolean(string='Es Cobrador', store=True)
    jjm_manager = fields.Many2one('res.partner', string="Encargado")


    #CONTRACT
    contract_ids = fields.One2many(
        comodel_name='contract.contract',
        inverse='partner_id',
        string="Contracts",
    )

    #DATOS DE LA TARJETA
    has_credit_card_jjm = fields.Boolean(string='Tiene tarjeta', store=True)
    credit_card_number_jjm = fields.Char(string='Numero de Tarjeta')
    bank_name_jjm = fields.Char(string='Nombre del Banco')

