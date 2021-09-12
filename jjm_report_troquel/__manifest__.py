# -*- coding: utf-8 -*-
{
    'name': 'JJM Report - Troquel',
    'description': '''
    Este modulo es el reporte del troquel.
    Debe seleccionar una factura asociada al cliente
     y cliquear en el Accion/Imprimir Troquel para imprimir el recibo.
    ''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'contacts',
        'sale',
        'product',
        'jjm_report_payment',
        ],
    'data': [
        'data/paperformat_data.xml',
        'report/troquel_view.xml',
    ],
    'application': False,
}
