from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    attendance_note = fields.Char(
        string="Attendance Note",
    )
