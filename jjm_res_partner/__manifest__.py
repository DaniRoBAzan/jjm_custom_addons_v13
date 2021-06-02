# -*- coding: utf-8 -*-

{
    'name': 'JJM Res Partner',
    'description': 'Add fields to the res_partner',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base','contacts'
        ],
    'data': [
        'views/res_partner_view.xml',
        'views/res_partner_purchase.xml',
    ],
    'application': False,
}
