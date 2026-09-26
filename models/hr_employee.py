from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_medical_technician = fields.Boolean(string="Is Medical Technician")
    certification_ids = fields.One2many("technician.certification", "employee_id", string="Certifications")
    equipment_work_order_ids = fields.One2many("equipment.work.order", "assigned_technician_id", string="Work Orders")