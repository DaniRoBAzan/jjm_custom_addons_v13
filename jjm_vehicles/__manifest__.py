# -*- coding: utf-8 -*-
{
    'name': 'JJM VEHICULOS',
    'description': '''
    Este modulo te ayudara a administrar los vehiculos con sus respectivas marcas y modelos.
    Ademas agrega un modelo de listado de precios.
    ''',
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
        'views/vehicles_price_view.xml',
        'data/fleet_cars_data.xml',
    ],
    'installable': True,
    'application': True,
}

