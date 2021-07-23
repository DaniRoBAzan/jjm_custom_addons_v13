{
    'name': 'JJM REPORTE DE COBRANZA',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este es el Reporte de Cobranzas, lo encontras en Ventas/Informes/Reporte Cobranza.
    El mismo permite elegir un cobrador o todos, descargando en pdf el reporte a partir de una fecha de inicio y otra de fin.
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base', 
                'sale',
                'account',
                'contract',
                'account_payment_group',
                'account_payment_group_document',
                ],
    'demo': [],
    'data': [
        # 'security/ir.model.access.csv',
        # 'report/template.xml',
        'report/report_payment_per_collector.xml',
        'wizard/wizard_payment_per_collector.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
