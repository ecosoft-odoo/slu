# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.constrains("operating_unit_id", "journal_id")
    def _check_journal_operating_unit(self):
        if not self._context.get("no_check_journal_ou"):
            res = super(AccountMove, self)._check_journal_operating_unit()
            return res