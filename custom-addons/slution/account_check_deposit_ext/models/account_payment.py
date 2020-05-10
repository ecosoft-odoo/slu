# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    number_check = fields.Char(
        string="Check No.",
    )
    date_check = fields.Date(
        string="Check Date",
    )
    check_deposit_id = fields.Many2one(
        comodel_name="account.check.deposit",
        compute="_compute_check_deposit_id",
        string="Check Deposit",
        store=True,
    )

    @api.depends("move_line_ids", "move_line_ids.check_deposit_id", "move_line_ids.check_deposit_id.state")
    def _compute_check_deposit_id(self):
        for rec in self:
            check_deposit = rec.move_line_ids.mapped("check_deposit_id")
            if check_deposit.state == "done":
                rec.check_deposit_id = check_deposit