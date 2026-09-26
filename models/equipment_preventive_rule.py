from odoo import fields, models, api

class EquipmentPreventiveRule(models.Model):
    _name = "equipment.preventive.rule"
    _description = "Manage the preventive rules"

    name = fields.Char()
    equipment_model_id = fields.Many2one("product.product", string="Equipment Model")
    interval_hours = fields.Float()