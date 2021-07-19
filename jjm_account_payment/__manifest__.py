# -*- coding: utf-8 -*-

{
    'name': 'JJM RECIBO CLIENTE',
    'description': '''
    Agrego cobrador en los recibos de clientes.
''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'account',
        'account_payment_group',
        'account_payment_group_document',
        ],
    'data': [
        'views/account_payment_group_view.xml',
    ],
    'application': False,
}
