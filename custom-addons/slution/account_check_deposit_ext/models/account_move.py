# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    number_check = fields.Char(
        string="Check No.",
        related="payment_id.number_check",
        store=True,
    )
    date_check = fields.Date(
        string="Check Date",
        related="payment_id.date_check",
        store=True,
    )