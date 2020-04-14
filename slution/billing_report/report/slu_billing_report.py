# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, tools


class SLUBillingReport(models.Model):
    _name = "slu.billing.report"
    _auto = False

    invoice_date = fields.Date()
    name = fields.Char()
    amount_untaxed = fields.Float()
    amount_total = fields.Float()
    invoice_date_due = fields.Date()
    communication = fields.Char()

    def _get_sql(self):
        sql = """
            SELECT am.id, am.invoice_date, am.name, am.amount_untaxed,
                   am.amount_total, am.invoice_date_due, null as communication
            FROM account_move am
            WHERE am.type IN ('out_invoice', 'out_refund') AND
                  am.state = 'posted' AND am.invoice_payment_state = 'not_paid'
        """
        return sql

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""CREATE OR REPLACE VIEW %s AS (%s)""" % (
            self._table, self._get_sql()))
