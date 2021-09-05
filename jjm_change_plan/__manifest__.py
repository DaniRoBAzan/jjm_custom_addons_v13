# -*- coding: utf-8 -*-
{
    'name': 'JJM CAMBIO DE PLAN',
    'description': '''
        Este modulo crea un boton en el contrato, que permite cambiar de plan,
        generando un nuevo contrato con los datos actuales, pero trasladando el numero de canon
        para identificar la cantidad de facturas pagadas.
    ''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'contract',
        'jjm_contract',
        'account_debt_management',
        'account_payment_group',
        'contract_state',
        ],
    'data': [
        'views/contract_view.xml',
    ],
    'application': False,
}

