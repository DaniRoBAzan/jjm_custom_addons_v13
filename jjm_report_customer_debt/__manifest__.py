{
    'name': 'JJM REPORTE DEUDA DE CLIENTE',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este es el Reporte de Deudas del cliente, lo encontras en Ventas/Informes/Reporte Cobranza.
    El mismo permite elegir un cliente y un contrato, 
    descargando en pdf el reporte con los datos ingresados.
    ''',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base',
                'account',
                'contract',
                'jjm_report_payment',
                ],
    'demo': [],
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_customer_debt.xml',
        'wizard/wizard_customer_debt.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
