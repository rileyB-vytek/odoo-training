{
    'name': 'Motorcycle Registry',
    'summary': """Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership
    of each motorcycled of the brand.""",
    'author': 'rileyB-vytek',
    'version': '0.1',
    'category': 'Kawaiil/Custom Modules',
    'website': 'https://github.com/rileyB-vytek/odoo-training',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_registry_menuitems.xml',
        'views/registry_views.xml',
    ],
    'demo': [
        'demo/registry_demo.xml',
    ],
    'application': True,
    'license': 'OPL-1',
}