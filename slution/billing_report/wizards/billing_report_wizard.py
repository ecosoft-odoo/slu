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
    report_ids = fields.Many2many(
        comodel_name="slu.billing.report",
        compute="_compute_report_ids",
    )

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except Exception:
            return []

    def _compute_report_ids(self):
        self.ensure_one()
        dom = [("salesperson_id", "=", self.salesperson_id.id)]
        if self.partner_id:
            dom += [("partner_id", "=", self.partner_id.id)]
        if self.date_from:
            dom += [("invoice_date_due", ">=", self.date_from)]
        if self.date_to:
            dom += [("invoice_date_due", "<=", self.date_to)]
        self.report_ids = self.env["slu.billing.report"].search(dom)

    def button_export_html(self):
        return True

    def button_export_pdf(self):
        self.ensure_one()
        action = self.env.ref("slution.action_slu_billing_report_pdf")
        return action.report_action(self, config=False)
