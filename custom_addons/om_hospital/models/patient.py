from odoo import api, fields, models


class HospitalPatient(models.Model):

    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string="Active", default=True)
    note = fields.Text(string="Description")
