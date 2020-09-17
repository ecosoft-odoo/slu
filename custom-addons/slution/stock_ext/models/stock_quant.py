# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    categ_id = fields.Many2one(
        comodel_name="product.category",
        string="Product Category",
        related="product_id.categ_id",
        store=True,
    )
    qty_minimum = fields.Float(
        string="Minimum Quantity",
        related="product_id.qty_minimum",
        store=True,
    )
    is_less_than_minimum_quantity = fields.Boolean(
        compute="_compute_is_less_than_minimum_quantity",
        store=True,
    )

    @api.depends("quantity", "qty_minimum")
    def _compute_is_less_than_minimum_quantity(self):
        for rec in self:
            if rec.quantity < rec.qty_minimum:
                rec.is_less_than_minimum_quantity = True
            else:
                rec.is_less_than_minimum_quantity = False
