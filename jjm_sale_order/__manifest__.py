# -*- coding: utf-8 -*-
{
    'name': 'JJM VENTAS',
    'description': '''
    Este modulo agrega un boton inteligente en la orden de venta confirmada, que calcula
    la cantidad de contratos por cada cliente, y brinda un acceso al listado de los mismos.
    ''',
    'author': "Romina Bazan",
    'website':  '',
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'sale',
        ],
    'data': [
        'views/sale_order_view.xml',
    ],
    'application': False,
}

