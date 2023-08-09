{
    'name': 'Odoo Academy',
    'summary': """Module to handle Course and Sessions""",
    'description': """Module to handle:
        - Courses
        - Sessions
        - Attendees
        """,
    'license': 'OPL-1',
    'author': 'rileyB-vytek',
    'website': 'https://github.com/rileyB-vytek/odoo-training',
    'category': 'Custom Modules/Tech Training',
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'views/academy_menuitems.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
    'version': '0.2',
}