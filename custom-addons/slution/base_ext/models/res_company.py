# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    partner_th = fields.Char()
    street_th = fields.Char()
    street2_th = fields.Char()
    city_th = fields.Char()
    state_th = fields.Char()
    zip_th = fields.Char()
    country_th = fields.Char()
