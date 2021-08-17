{
    'name': 'JJM REPORTE DE BAJA',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este modulo imprime  el Reporte de Baja del Cliente.
    Permite seleccionar:
    - Fecha Inicial
    - Fecha Final
    - Supervisor
    - Vendedor
    - Campana
    y al imprimir  genera el reporte donde se podrá visualizar:
    CLIENTE - CONTRATO -  FECHA BAJA - MOTIVO DE LA BAJA
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base', 
                'sale',
                'account',
                'jjm_contract',
                'jjm_report_payment',
                ],
    'demo': [],
    'data': [
        #'security/ir.model.access.csv',
        'report/report_unsubscribe.xml',
        'wizard/wizard_unsubscribe.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
