from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        invoice_vals = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(
            order, name, amount, so_line)
        journal = self.env['account.move'].with_context(default_type='out_invoice')._get_default_journal()
        if order.operating_unit_id and journal.operating_unit_id != order.operating_unit_id:
            journal = self.env["account.journal"].search([("type", "=", journal.type)])
            jf = journal.filtered(
                lambda aj: aj.operating_unit_id == order.operating_unit_id
            )
            if not jf:
                journal_id = journal[0].id
            else:
                journal_id = jf[0].id
            invoice_vals["journal_id"] = journal_id
        invoice_vals["operating_unit_id"] = order.operating_unit_id.id
        return invoice_vals