# -*- coding: utf-8 -*-
{
    'name': 'JJM CONTABILIDAD / FACTURACION',
    'description': '''
    Este modulo agrega:
    - el canon, Asesor / Vendedor, Cobrador, Campaña, Forma de pago 
    y numero de contrato al encabezado de las facturas (este en Otra informacion, Documento origen).
    - filtros, agrupacion de los mismos.
    ''',
    'author': "Romina Bazan",
    'website':  '',
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'account',
        "account_payment_fix",
        "account_payment_group",
        "jjm_change_plan",
        ],
    'data': [
        'views/account_view.xml',
    ],
    'application': False,
}

