from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
    _name = "motorcycle_registry.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"
    _sql_constraints = [ ('vin','UNIQUE(vin)','VIN number already exists'), ]
    
    registry_number = fields.Char(string="Motorcycle Registry Number (MRN)", default="MRN0000", copy=False, required=True, readonly=True)
    
    vin = fields.Char(string="VIN", required=True)
    make = fields.Char(string="Make", readonly=True, compute="_compute_make")
    model = fields.Char(string="Model", readonly=True, compute="_compute_model")
    year = fields.Char(string="Year", readonly=True, compute="_compute_year")
    
    license_plate = fields.Char(string="License Plate")

    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner")
    #first_name = fields.Char(string="First", required=True)
    #last_name = fields.Char(string="Last", required=True)
    email = fields.Char(related="owner_id.email")
    phone = fields.Char(related="owner_id.phone")
    
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
                
    @api.constrains("vin")
    def _check_vin_pattern(self):
        for registry in self.filtered(lambda r: r.vin):
            match = re.match("^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{6}$", registry.vin)
            if not match:
                raise ValidationError("""The VIN must match the specified pattern.
                ● Make - 2 Capital Letters
                ● Model - 2 Capital Letters
                ● Year - 2 Digits
                ● Battery Capacity - 2 Capital Letters or Numbers
                ● Serial Number - 6 Digits""")
                
    @api.constrains("license_plate")
    def _check_license_plate_pattern(self):
        for registry in self.filtered(lambda r: r.license_plate):
            match = re.match("^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$", registry.license_plate)
            if not match:
                raise ValidationError("""The License Plate must match the specified pattern.
                ● 1 - 4 Capital Letters
                ● 1 - 3 Digits
                ● Optional 2 Capital Letters""")
    
    @api.depends("vin")
    def _compute_make(self):
        for record in self:
            if record.vin:
                # Use regex to grab make portion of VIN (Make = first 2 capital letters)
                record.make = record.vin[:1] + record.vin[1:2]
                
    @api.depends("vin")
    def _compute_model(self):
        for record in self:
            if record.vin:
                # Use regex to grab model portion of VIN (Make = second 2 capital letters)
                record.model = record.vin[2:3] + record.vin[3:4]
                
    @api.depends("vin")
    def _compute_year(self):
        for record in self:
            if record.vin:
                # Use regex to grab year portion of VIN (Make = first 2 digits)
                record.year = record.vin[4:5] + record.vin[5:6]

                