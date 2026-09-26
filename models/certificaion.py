from odoo import fields, models, api

class Certification(models.Model):
    _name = "technician.certification"
    _description = "Manage the certification"

    certification_name = fields.Char(required=True)
    issuing_body = fields.Text()
    expiry_date = fields.Date()
    is_valid = fields.Boolean(compute='_compute_is_valid')
    employee_id = fields.Many2one("hr.employee")

    @api.depends('expiry_date')
    def _compute_is_valid(self):
        today = fields.Date.today()
        for record in self:
            if record.expiry_date:
                record.is_valid = record.expiry_date >= today
            else:
                record.is_valid = False