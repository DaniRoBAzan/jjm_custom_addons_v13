# -*- coding: utf-8 -*-
{
    'name': 'JJM Vehicles',
    'description': 'With this module, Odoo helps you managing all your vehicles.',
    'summary': 'Manage your vehicles',
    'author': "Romina Bazan",
    'website':  '',
    'license': 'OEEL-1',
    'version':  '14.0.1.0',
    'depends': [
        'base',
        'mail',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_views.xml',
        'data/fleet_cars_data.xml',
    ],
    'installable': True,
    'application': True,
}
