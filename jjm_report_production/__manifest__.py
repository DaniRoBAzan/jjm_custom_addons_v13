{
    'name': 'JJM REPORTE DE PRODUCCION',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este es el Reporte de Produccion, lo encontras en Contacto/Informes/Reporte Produccion.
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base', 
                'sale',
                'account',
                'contract',
                ],
    'demo': [],
    'data': [
        #'security/ir.model.access.csv',
        'report/report_production.xml',
        'wizard/wizard_production.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
