# -*- coding: utf-8 -*-
{
    'name': 'JJM CONTRATOS',
    'description': '''
    -Agrego campo Estado Deuda en el formulario de cliente: el mismo agrega automáticamente un estado "Al dia" si el cliente tiene seteado el campo Debt Balance en 0 o negativo ; de lo contrario, lo declara como un estado "Adeuda" .
    -Agrego agrupación por "Estado de deuda" y filtrado por "Al día" - "Adeuda".
    -Agrego en contrato el campo Fecha Adhesión y el nombre del contrato se convierte en secuencial de 6 digitos arrancando con las siglas JJM.
    -Agrego modelo de Campaña, el cual tiene una relacion en el contrato.
    -Agrego modelo de Forma de Pago, el cual tiene una relacion en el contrato.
    -Agrego cobrador al contrato, el mismo se habilita al asignar una forma de pago "cobrador".

''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'contract',
        'account_debt_management',
        ],
    'data': [
        'security/ir.model.access.csv',
        'data/contract_seq_data.xml',
        'views/method_payment_view.xml',
        'views/campaign_view.xml',
        'views/contract_view.xml',
        'views/partner_view.xml',
    ],
    'application': False,
}

