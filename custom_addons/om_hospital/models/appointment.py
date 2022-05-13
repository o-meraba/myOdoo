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
    ref = fields.Char(string="Reference", help="Reference of the patient from patient record")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')],default='draft', string="Status", required=True, tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_test(self):
        print("Test Button clicked")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "Click Successfull",
                'type': 'rainbow_man',
            }
        }

    def action_button(self):
        print("Action button was clicked")


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

