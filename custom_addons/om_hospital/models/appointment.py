from odoo import api, fields, models


class HospitalAppointment(models.Model):

    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient") # you can use just 'hospital.patient' but it should place first in parentheses
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.today)
    gender = fields.Selection(related='patient_id.gender')
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string='Prescription')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

