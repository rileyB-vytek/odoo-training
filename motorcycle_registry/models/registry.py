from odoo import fields, models

class Registry(models.Model):
    _name = "motorcycle_registry.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    registry_number = fields.Char(string="Registry Number", required=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First", required=True)
    last_name = fields.Char(string="Last", required=True)
    image = fields.Image(string="Image")
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Binary(string="Certificate Title")
    register_date = fields.Date(string="Register Date")