from odoo import api, fields, models
import re

class Registry(models.Model):
    _name = "motorcycle_registry.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    registry_number = fields.Char(string="Motorcycle Registry Number (MRN)", default="MRN0000", copy=False, required=True, readonly=True)
    
    vin = fields.Char(string="VIN", compute="_compute_registry_vin", required=True, readonly=True)
    make = fields.Char(string="Make", required=True)
    model = fields.Char(string="Model", required=True)
    year = fields.Char(string="Year", required=True)
    battery_capacity = fields.Char(string="Battery Capacity", required=True)
    serial_number = fields.Char(string="Serial Number", required=True)
    
    license_plate = fields.Char(string="License Plate")
    
    first_name = fields.Char(string="First", required=True)
    last_name = fields.Char(string="Last", required=True)
    image = fields.Image(string="Image")
    current_mileage = fields.Float(string="Current Mileage")
    certificate_title = fields.Binary(string="Certificate Title")
    register_date = fields.Date(string="Register Date")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.depends("make", "model", "year", "battery_capacity", "serial_number")
    def _compute_session_duration(self):
        for record in self:
            if record.make and record.model and record.year and record.battery_capacity and record.serial_number:
                record.vin = re.match("[A-Z]{2}", record.make) + re.match("[A-Z]{2}", record.model) + re.match("\d{2}", record.year) + re.match("[A-Z0-9]{2}", record.battery_capacity) + re.match("\d{5}", record.serial_number)
                