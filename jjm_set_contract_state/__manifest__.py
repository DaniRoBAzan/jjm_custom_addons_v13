# -*- coding: utf-8 -*-
{
    'name': 'JJM SETEO ESTADO CONTRATO',
    'description': '''
    Este modulo crea una accion planificada que se activa automaticamente,
    busca si el cliente de cada contrato adeuda 3 o mas facturas y setea 
    el estado del contrato a Baja, ademas de agregar a su motivo de baja 
    la leyenda: Baja dada por sistema, el cliente supera las 3 facturas vencidas.
''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'contract',
        'account_debt_management',
        'account_payment_group',
        'contract_state',
        ],
    'data': [
        'data/data.xml',
    ],
    'application': False,
}

