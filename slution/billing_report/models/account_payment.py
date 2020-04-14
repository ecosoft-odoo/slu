# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    is_installment = fields.Boolean(
        string="Is Installment ?",
        default=False,
    )
    installment_invoice_id = fields.Many2one(
        comodel_name="account.move",
        string="Invoice Ref",
    )

    @api.onchange("installment_invoice_id")
    def _onchange_installment_invoice_id(self):
        if self.installment_invoice_id:
            self.salesperson_id = self.installment_invoice_id.salesperson_id

    @api.onchange('is_installment')
    def _onchange_is_installment(self):
        self.installment_invoice_id = False
