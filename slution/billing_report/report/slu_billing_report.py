# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, tools


class SLUBillingReport(models.Model):
    _name = "slu.billing.report"
    _auto = False

    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
    )
    invoice_date = fields.Date()
    name = fields.Char()
    amount_total = fields.Float()
    invoice_date_due = fields.Date()
    communication = fields.Char()

    def _get_sql(self):
        sql = """
            SELECT ROW_NUMBER() over(ORDER BY am.id, ap.id) as id,
                   am.salesperson_id, am.partner_id, am.invoice_date, am.name,
                   (CASE WHEN am.type = 'out_invoice' THEN 1 ELSE -1 END) *
                   (CASE WHEN am.is_installment = False THEN am.amount_total
                   ELSE ap.amount END) AS amount_total,
                   CASE WHEN am.is_installment = False THEN am.invoice_date_due
                   ELSE ap.payment_date END AS invoice_date_due,
                   CASE WHEN am.is_installment = False THEN NULL
                   ELSE ap.communication END AS communication
            FROM account_move am
            LEFT JOIN account_payment ap ON am.id = ap.installment_invoice_id
            AND ap.state = 'draft'
            WHERE am.type IN ('out_invoice', 'out_refund') AND
                  am.state = 'posted' AND am.invoice_payment_state = 'not_paid'
        """
        return sql

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""CREATE OR REPLACE VIEW %s AS (%s)""" % (
            self._table, self._get_sql()))
