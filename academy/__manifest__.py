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
    'depends': ['sale', 'website'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'views/academy_web_templates.xml',
        'wizard/sale_wizard_view.xml',
        'reports/session_report_templates.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
    'version': '0.2',
    'auto_install': True,
}