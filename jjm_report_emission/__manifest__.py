{
    'name': 'JJM REPORTE DE EMISION',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este es el Reporte Emision.
    Permite seleccionar un cobrador(o todos) y un mes.
    Trae todas las facturas emitidas por cobrador/es en el mes seleccionado.
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base',
                'sale',
                'account',
                'contract',
                'jjm_account_payment',
                'jjm_report_payment',
                ],
    'demo': [],
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_emission.xml',
        'wizard/wizard_emission.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
