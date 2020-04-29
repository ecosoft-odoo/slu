# © 2019 Eficent Business and IT Consulting Services S.L.
# - Jordi Ballester Alomar
# © 2019 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _default_operating_unit(self):
        team = self.env["crm.team"]._get_default_team_id()
        if team.operating_unit_id:
            return team.operating_unit_id
        return self.env.user.default_operating_unit_id

    operating_unit_id = fields.Many2one(
        comodel_name="operating.unit",
        string="Operating Unit",
        default=_default_operating_unit,
        readonly=True,
        states={"draft": [("readonly", False)], "sent": [("readonly", False)]},
    )

    @api.onchange("team_id")
    def onchange_team_id(self):
        if self.team_id:
            self.operating_unit_id = self.team_id.operating_unit_id

    @api.onchange("operating_unit_id")
    def onchange_operating_unit_id(self):
        if self.team_id and self.team_id.operating_unit_id != self.operating_unit_id:
            self.team_id = False

    @api.constrains("team_id", "operating_unit_id")
    def _check_team_operating_unit(self):
        for rec in self:
            if rec.team_id and rec.team_id.operating_unit_id != rec.operating_unit_id:
                raise ValidationError(
                    _(
                        "Configuration error. The Operating "
                        "Unit of the sales team must match "
                        "with that of the quote/sales order."
                    )
                )

    @api.constrains("operating_unit_id", "company_id")
    def _check_company_operating_unit(self):
        for rec in self:
            if (
                rec.company_id
                and rec.operating_unit_id
                and rec.company_id != rec.operating_unit_id.company_id
            ):
                raise ValidationError(
                    _(
                        "Configuration error. The Company in "
                        "the Sales Order and in the Operating "
                        "Unit must be the same."
                    )
                )

    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        journal_id = invoice_vals.get("journal_id")
        if not journal_id:
            journal = self.env["account.move"].with_context(default_type="out_invoice")._get_default_journal()
        else:
            journal = self.env["account.journal"].browse(journal_id)
        if self.operating_unit_id and journal.operating_unit_id != self.operating_unit_id:
            journal = self.env["account.journal"].search([("type", "=", journal.type)])
            jf = journal.filtered(
                lambda aj: aj.operating_unit_id == self.operating_unit_id
            )
            if not jf:
                journal_id = journal[0].id
            else:
                journal_id = jf[0].id
            invoice_vals["journal_id"] = journal_id
        invoice_vals["operating_unit_id"] = self.operating_unit_id.id
        return invoice_vals


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    operating_unit_id = fields.Many2one(
        related="order_id.operating_unit_id", string="Operating Unit"
    )
