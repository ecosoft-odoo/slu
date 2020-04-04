# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        if vals.get("operating_unit_id", False):
            sequence_code = (
                self.env["operating.unit"]
                .browse(vals["operating_unit_id"])
                .so_sequence_id
                .code
            )
            if sequence_code:
                vals["name"] = self.env["ir.sequence"].next_by_code(sequence_code)
        return super().create(vals)
