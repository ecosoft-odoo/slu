from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        ctx = self._context.copy()
        ctx["no_check_journal_ou"] = True
        invoice = super(SaleAdvancePaymentInv, self.with_context(ctx))._create_invoice(
            order, so_line, amount
        )
        invoice_ctx = invoice._context.copy()
        invoice_ctx["no_check_journal_ou"] = False
        invoice = invoice.with_context(invoice_ctx)
        invoice_vals = {"operating_unit_id": order.operating_unit_id}
        invoice_line_vals = invoice_vals
        if order.operating_unit_id and invoice.journal_id.operating_unit_id != order.operating_unit_id:
            journal = self.env["account.journal"].search([("type", "=", invoice.journal_id.type)])
            jf = journal.filtered(
                lambda aj: aj.operating_unit_id == order.operating_unit_id
            )
            if not jf:
                journal_id = journal[0].id
            else:
                journal_id = jf[0].id
            invoice_vals["journal_id"] = journal_id
        invoice.write(invoice_vals)
        invoice.line_ids.write(invoice_line_vals)
        return invoice