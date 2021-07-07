# -*- coding: utf-8 -*-

{
    'name': 'JJM Contract',
    'description': 'Add fields to the contract',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'contract',
        'account_debt_management',
        # 'product',
        ],
    'data': [
        'data/contract_seq_data.xml',
        'views/contract_view.xml',
        'views/partner_view.xml',
    ],
    'application': False,
}
