from odoo import fields, models

class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    image = fields.Image(string="Image")
    
    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner','Beginner'),
                                 ('intermediate','Intermediate'),
                                 ('advanced','Advanced'),
                             ],
                             copy=False)