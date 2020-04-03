# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    user_id = fields.Many2one(
        string="Salesperson (not used)",
    )
    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
    )

    def _query(self, with_clause="", fields={}, groupby="", from_clause=""):
        fields["salesperson_id"] = ", s.salesperson_id as salesperson_id"
        groupby += ", s.salesperson_id"
        return super(SaleReport, self)._query(
            with_clause=with_clause, fields=fields, groupby=groupby,
            from_clause=from_clause)
