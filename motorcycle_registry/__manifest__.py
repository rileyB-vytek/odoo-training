{
    'name': 'Motorcycle Registry',
    'summary': """Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership
    of each motorcycled of the brand.""",
    'author': 'rileyB-vytek',
    'version': '0.2',
    'category': 'Kawaiil/Custom Modules',
    'website': 'https://github.com/rileyB-vytek/odoo-training',
    'depends': ['base', 'stock'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/registry_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_views_inherit.xml',
    ],
    'demo': [
        'demo/registry_demo.xml',
    ],
    'application': True,
    'license': 'OPL-1',
}