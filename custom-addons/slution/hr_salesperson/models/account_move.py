# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_user_id = fields.Many2one(
        string="Salesperson (not used)",
    )
    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        domain=lambda self: self._get_domain_salesperson_id(),
    )

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except Exception:
            return []
