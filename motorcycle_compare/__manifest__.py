{
    'name': 'Motorcycle Compare',
    'summary': """Module to view and compare difference Motorcycle Models""",
    'description': """Module includes:
        - Website page to compare all different motorcycle models
        - View model specs, features and power
        """,
    'license': 'OPL-1',
    'author': 'rileyB-vytek',
    'website': 'https://github.com/rileyB-vytek/odoo-training',
    'category': 'Custom Modules/Tech Training',
    'depends': ['base', 'stock', 'website'],
    'data': [
        'views/motorcycle_compare_templates.xml',
    ],
    'demo': [
    ],
    'application': True,
    'version': '0.1',
    'auto_install': True,
}