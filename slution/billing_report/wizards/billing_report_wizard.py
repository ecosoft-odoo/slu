# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class BillingReportWizard(models.TransientModel):
    _name = "billing.report.wizard"

    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        domain=lambda self: self._get_domain_salesperson_id(),
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )
    date_from = fields.Date()
    date_to = fields.Date()

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except Exception:
            return []

    def button_export_html(self):
        return True

    def button_export_pdf(self):
        return True
