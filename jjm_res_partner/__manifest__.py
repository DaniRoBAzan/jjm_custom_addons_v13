# -*- coding: utf-8 -*-

{
    'name': 'JJM CONTACTOS',
    'description': '''
    - Agrego solapa de informacion laboral con los datos de la empresa
    - Agrego solapa de informacion personal 
    - Agrego el campo Documentos a la vista tree
    - cambio nombre de campos de origen por Ocupacion y Barrio.
    - Agrego campos en solapa Compra y Ventas: Es Socio, Es Supervisor, Es Asesor / Vendedor,
    Codigo Asesor, Es Cobrador  y Encargado.
    - En Contrato/Partner/Facturacion y Contabilidad, se te habilita la opción "Tiene tarjeta", 
    al tildar aparece la opción de cargar los datos del banco y numero de tarjeta.
    ''',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'contacts',
        'partner_manual_rank',
        'partner_contact_gender',
        'partner_contact_personal_information_page',
        'partner_contact_birthdate',
        'contract'
        ],
    'data': [
        'views/res_partner_view.xml',
        'views/res_partner_purchase.xml',
    ],
    'application': False,
}
