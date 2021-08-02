# -*- coding: utf-8 -*-
{
    'name': 'JJM ACTUALIZACION DE PRECIOS',
    'description': '''
    Este modulo actualiza los precios de lista de los kits.
    En la linea de las tarifas agrega un campo %a imputar, a partir del cual calcula el nuevo precio.
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
        #'security/ir.model.access.csv',
        'views/product_pricelist_view.xml',
    ],
    'application': False,
}

