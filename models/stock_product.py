from odoo import fields , models , api


class Stock_product(models.Model):

    _inherit = "product.product"

    rule_id = fields.One2many("equipment.preventive.rule" , "equipment_model_id")