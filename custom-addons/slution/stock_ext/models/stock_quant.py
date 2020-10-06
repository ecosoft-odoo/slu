# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class StockQuant(models.Model):
    _inherit = "stock.quant"

    categ_id = fields.Many2one(
        comodel_name="product.category",
        string="Product Category",
        related="product_id.categ_id",
        store=True,
    )
