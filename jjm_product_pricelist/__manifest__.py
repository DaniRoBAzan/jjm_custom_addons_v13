# -*- coding: utf-8 -*-
{
    'name': 'JJM PRECIOS DE LISTA',
    'description': '''
    this module makes improvements in the product pricelist.
    ''',
    'author': "Romina Bazan",
    'website':  '',
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'product',
        ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_pricelist_wizard.xml',
    ],
    'application': False,
}

