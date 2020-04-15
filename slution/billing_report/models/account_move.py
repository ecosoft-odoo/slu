# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    is_installment = fields.Boolean(
        string="Is Installment ?",
        default=False,
        copy=False,
    )
