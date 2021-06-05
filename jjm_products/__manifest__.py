# -*- coding: utf-8 -*-

{
    'name': 'JJM Products',
    'description': 'Add fields to the product_template',
    'author': "Romina Bazan",
    'license': 'OEEL-1',
    'version':  '1.0',
    'depends': [
        'base',
        'product',
        'jjm_vehicles',
        # 'partner_manual_rank',
        # 'partner_contact_personal_information_page',
        # 'partner_contact_birthdate'
        ],
    'data': [
        'views/product_view.xml',
        # 'views/res_partner_purchase.xml',
    ],
    'application': False,
}
