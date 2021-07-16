{
    'name': 'JJM Report Payment',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Reporte de Cobranzas',
    'license': 'AGPL-3',
    'author': 'Romina Bazan',
    'maintainer': 'Romina Bazan',
    'depends': ['base', 
                'sale', ],
    'demo': [],
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/view.xml',
        'report/template.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
