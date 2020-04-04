# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.model
    def create(self, vals):
        if vals.get("operating_unit_id", False):
            ou = self.env["operating.unit"].browse(vals["operating_unit_id"])
            if self.payment_type == 'transfer':
                sequence_code = ou.payment_transfer_seq_id.code
            else:
                if self.partner_type == 'customer':
                    if self.payment_type == 'inbound':
                        sequence_code = ou.payment_cust_inv_seq_id.code
                    if self.payment_type == 'outbound':
                        sequence_code = ou.payment_cust_refund_seq_id.code
                if self.partner_type == 'supplier':
                    if self.payment_type == 'inbound':
                        sequence_code = ou.payment_supp_refund_seq_id.code
                    if self.payment_type == 'outbound':
                        sequence_code = ou.payment_supp_inv_seq_id.code
            if sequence_code:
                vals["name"] = self.env["ir.sequence"].next_by_code(sequence_code)
        return super().create(vals)
