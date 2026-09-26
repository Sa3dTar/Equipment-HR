from odoo import fields, models, api

class EquipmentWorkOrder(models.Model):
    _name = "equipment.work.order"
    _description = "Manage the equipment work orders"

    name = fields.Char(required=True, copy=False, readonly=True, default=lambda self: ('New'))
    equipment_id = fields.Many2one("stock.lot", string="Equipment")
    failure_type = fields.Selection([
        ("breakdown", "Breakdown"),
        ("preventive", "Preventive")
    ])
    assigned_technician_id = fields.Many2one(
        "hr.employee",
        string="Assigned Technician",
        domain=[("is_medical_technician", "=", True)]
    )
    state = fields.Selection([
        ("draft", "Draft"),
        ("assigned", "Assigned"),
        ("waiting_parts", "Waiting Parts"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled")
    ], default="draft")
    start_date_time = fields.Datetime()
    end_date_time = fields.Datetime()
    downtime_hours = fields.Float(compute="_compute_downtime_hours", store=True)
    
    @api.depends("start_date_time", "end_date_time")
    def _compute_downtime_hours(self):
        for record in self:
            if record.start_date_time and record.end_date_time:
                duration = record.end_date_time - record.start_date_time
                record.downtime_hours = duration.total_seconds() / 3600
            else:
                record.downtime_hours = 0.0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', ('New')) == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('equipment.work.order') or ('New')
        return super().create(vals_list)