# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


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

    def _get_html(self):
        result = {}
        rcontext = {}
        report = self.browse(self._context.get("active_id"))
        if report:
            rcontext["o"] = report
            result["html"] = self.env.ref(
                "slution.slu_billing_report_html"
            ).render(rcontext)
        return result

    @api.model
    def get_html(self, given_context=None):
        return self.with_context(given_context)._get_html()

    def button_export_html(self):
        self.ensure_one()
        action = self.env.ref("slution.action_slu_billing_report_html")
        vals = action.read()[0]
        context = vals.get("context", {})
        if context:
            context = safe_eval(context)
        context.update({
            "active_id": self.id,
            "active_ids": self.ids,
        })
        vals["context"] = context
        return vals

    def button_export_pdf(self):
        self.ensure_one()
        action = self.env.ref("slution.action_slu_billing_report_pdf")
        return action.report_action(self, config=False)
