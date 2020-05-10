# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api
from collections import defaultdict
from odoo.addons.account.models.account_payment import \
    MAP_INVOICE_TYPE_PARTNER_TYPE


class AccountPayment(models.Model):
    _inherit = "account.payment"

    salesperson_id = fields.Many2one(
        comodel_name="hr.employee",
        domain=lambda self: self._get_domain_salesperson_id(),
    )

    @api.model
    def default_get(self, default_fields):
        res = super().default_get(default_fields)
        context = self._context
        active_ids = context.get("active_ids")
        active_model = context.get("active_model")
        if not active_ids or active_model != "account.move":
            return res
        invoices = self.env[active_model].browse(active_ids)
        res.update({
            "salesperson_id": invoices[0].salesperson_id.id,
        })
        return res

    @api.model
    def _get_domain_salesperson_id(self):
        try:
            return [("department_id", "=", self.env.ref("hr.dep_sales").id)]
        except Exception:
            return []


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def get_payments_vals(self):
        '''Compute the values for payments.

        :return: a list of payment values (dictionary).
        '''
        grouped = defaultdict(lambda: self.env["account.move"])
        for inv in self.invoice_ids:
            if self.group_payment:
                grouped[(
                    inv.commercial_partner_id, inv.currency_id,
                    inv.invoice_partner_bank_id,
                    MAP_INVOICE_TYPE_PARTNER_TYPE[inv.type],
                    inv.salesperson_id)] += inv
            else:
                grouped[inv.id] += inv
        return [self._prepare_payment_vals(invoices)
                for invoices in grouped.values()]

    def _prepare_payment_vals(self, invoices):
        res = super()._prepare_payment_vals(invoices)
        res.update({
            "salesperson_id": invoices[0].salesperson_id.id,
        })
        return res
