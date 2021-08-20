{
    'name': 'JJM REPORTE DE MOROSOS',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': '''
    Este modulo imprime  el Reporte de Morosos, lo encontras en Contacto/Informes/Reporte Produccion.
    Permite seleccionar:
    - Supervisor
    - Cliente
    y al imprimir  genera el reporte donde se podrá visualizar:
    NRO - CLIENTE - TELEFONO - DIRECCION - HORARIO -  FECHA - IMPORTE ADEUDADO
    Trae las facturas del o los clientes que tengan facturas impagas 
    con fecha de vencimiento > 15 en  estado publicado
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
        'report/report_defaulter.xml',
        'wizard/wizard_defaulter.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
