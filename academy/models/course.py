from odoo import api, fields, models
from odoo.exceptions import ValidationError
class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"

    #Reserved Fields
    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    # Simple Fields
    image = fields.Image(string="Image")
    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[('beginner','Beginner'),
                                 ('intermediate','Intermediate'),
                                 ('advanced','Advanced'),],
                             copy=False)

    session_ids = fields.One2many(comodel_name="academy.session", string="Session", inverse_name="course_id")

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", default= lambda self:self.env.company.currency_id.id)

    base_price = fields.Monetary(string="Base Price", currency_field="currency_id")
    additional_fee = fields.Monetary(string="Additional Fee", currency_field="currency_id")
    total_price = fields.Monetary(string="Total Price", currency_field="currency_id", compute="_compute_total_price")

    @api.depends("base_price", "additional_fee")
    def _compute_total_price(self):
        for record in self:
            if(record.base_price < 0):
                raise ValidationError(('Base Price can not be negative'))
            record.total_price = record.base_price + record.additional_fee
        