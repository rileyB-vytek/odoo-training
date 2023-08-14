from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils


class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    name = fields.Char(string="Title", related="course_id.name", readonly=False)
    
    session_number = fields.Char(string="Session Number", default="S0000", copy=False, required=True, readonly=True)
    
    date_start = fields.Datetime(string="Start Date", required=True)
    
    date_end = fields.Datetime(string="End Date", required=True)

    duration = fields.Integer(string="Session Duration", compute="_compute_session_duration", inverse="_inverse_session_duration", readonly=False)
    
    course_id = fields.Many2one(comodel_name="academy.course", string="Course", ondelete="cascade", required=True)

    instructor_id = fields.Many2one(comodel_name="res.users", string="Instructor", ondelete="restrict")

    student_ids = fields.Many2many(comodel_name="res.partner", string="Students")

    description = fields.Text(related="course_id.description")

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", default= lambda self:self.env.company.currency_id.id)
    
    total_price = fields.Monetary(string="Total Price", currency_field="currency_id", related="course_id.total_price")
    
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

    @api.depends("date_start", "date_end")
    def _compute_session_duration(self):
        for record in self:
            if record.date_start and record.date_end:
                record.duration = (record.date_end - record.date_start).days + 1
        
    def _inverse_session_duration(self):
        for record in self:
            if record.date_start and record.duration:
                record.date_end = date_utils.add(record.date_start, days=record.duration-1)
                
