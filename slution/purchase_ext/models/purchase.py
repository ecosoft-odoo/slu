# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_name = fields.Char(
        related='partner_id.name',
    )
