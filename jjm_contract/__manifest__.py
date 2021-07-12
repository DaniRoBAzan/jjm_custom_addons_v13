# -*- coding: utf-8 -*-

{
    'name': 'JJM Contract',
    'description': '''
    Agregue campo Estado deuda en el formulario de cliente, el mismo agrega automáticamente un estado "Al dia" si el cliente tiene seteado el campo Debt Balance en 0 o negativo ; de lo contrario, lo declara como un estado "Adeuda" .
    Ademas agrego agrupación por "Estado de deuda" y filtrado por "Al día" - "Adeuda".
    En el contrato agrega el campo Fecha Adhesión y el nombre del contrato se convierte en secuencial de 6 digitos arrancando con las siglas JJM.
''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'contract',
        'account_debt_management',
        # 'product',
        ],
    'data': [
        'data/contract_seq_data.xml',
        'views/contract_view.xml',
        'views/partner_view.xml',
    ],
    'application': False,
}
