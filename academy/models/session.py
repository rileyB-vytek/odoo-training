from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    name = fields.Char(string="Title")
    session_number = fields.Char(string="Session Number", default="S0000", copy=False, required=True, readonly=True)
    
    date_start = fields.Datetime(string="Start Date", required=True)
    
    date_end = fields.Datetime(string="End Date", required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('session_number', ('S0000')) == ('S0000'):
                vals['session_number'] = self.env['ir.sequence'].next_by_code('session.number')
        return super().create(vals_list)

    @api.constrains('date_start', 'date_end')
    def _check_end_date(self):
        for session in self:
            if(session.date_start > session.date_end):
                raise ValidationError('The end date can not be before the start date!')