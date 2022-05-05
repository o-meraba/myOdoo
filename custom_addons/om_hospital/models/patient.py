from odoo import api, fields, models


class HospitalPatient(models.Model):

    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(string="Name", tracking=True)
    age = fields.Integer(string="Age")
    ref = fields.Char(string="Reference", default='HB00')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string='Gender', default='male')
    active = fields.Boolean(string="Active", default=True)
    note = fields.Text(string="Description", tracking=True)
