{
    'name': 'JJM REPORTE DE PRODUCCION',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este modulo imprime  el Reporte de Produccion, lo encontras en Contacto/Informes/Reporte Produccion.
    Permite seleccionar:
    - Vendedor
    - Campana
    y al imprimir  genera el reporte donde se podrá visualizar:
    CLIENTE - CONTRATO -  FECHA ADHESION - IMPORTE
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
