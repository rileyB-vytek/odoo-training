from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle')
    ], ondelete={'motorcycle': 'set product'})
    
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')
    curb_weight = fields.Float(string='Curb Weight')
    launch_date = fields.Date(string='Launch Date')

    horsepower = fields.Float(string='Horsepower')
    top_speed = fields.Float(string='Top Speed')
    torque = fields.Float(string='Torque')
    
    battery_capacity = fields.Selection(string='Battery Capacity',
                             selection=[('small','Small'),
                                 ('medium','Medium'),
                                 ('large','Large'),
                                 ('extra_large','Extra Large'),],
                             copy=False)
    charge_time = fields.Float(string='Charge Time')
    range = fields.Float(string='Range')

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping