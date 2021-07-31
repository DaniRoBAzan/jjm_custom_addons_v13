# -*- coding: utf-8 -*-
{
    'name': 'JJM PRODUCTOS MOTO/COMBO',
    'description': '''
    Modulo que permite agregar modelos y marcas a un producto.
     -Se debe seleccionar el tipo de producto, una moto o un combo.
     
     Ademas agrega las tarifas a los productos con los campos:
    -Nombre tarifa
    -Moneda  
    -Modelo 
    -Precio 
    -Fecha inicial  
    -Fecha final  
    **Desde el Modelo se puede acceder a la lista de precios de cada producto.
    
    ''',
    'author': "Romina Bazan",
    'website':  '',
    'license': 'OEEL-1',
    'version':  '14.0.1.0',
    'depends': [
        'base',
        'mail',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_views.xml',
        'views/vehicles_price_view.xml',
        'data/fleet_cars_data.xml',
    ],
    'installable': True,
    'application': True,
}

