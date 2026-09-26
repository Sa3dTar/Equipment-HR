from odoo import fields , models , api


class Stock_lot(models.Model):

    _inherit = "stock.lot"

    work_order_id = fields.One2many("equipment.work.order" ,"equipment_id")