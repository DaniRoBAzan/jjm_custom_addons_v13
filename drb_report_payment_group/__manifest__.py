{
    'name': 'DRB Report Payment Group',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este modulo reemplaza al reporte de Recibo de Cliente.
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base', 
                'account_payment_group',
                ],
    'demo': [],
    'data': [
        'report/report_payment_group.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
