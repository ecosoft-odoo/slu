# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    qty_minimum = fields.Float(
        string="Minimum Quantity",
        digits="Product Unit of Measure",
        default=0.0,
    )
    is_less_than_minimum_quantity = fields.Boolean(
        compute="_compute_is_less_than_minimum_quantity",
        store=True,
    )

    @api.depends("qty_available", "qty_minimum")
    def _compute_is_less_than_minimum_quantity(self):
        for rec in self:
            if rec.qty_available < rec.qty_minimum:
                rec.is_less_than_minimum_quantity = True
            else:
                rec.is_less_than_minimum_quantity = False


class ProductTemplate(models.Model):
    _inherit = "product.template"

    qty_minimum = fields.Float(
        string="Minimum Quantity",
        compute="_compute_qty_minimum",
        inverse="_set_qty_minimum",
        digits="Product Unit of Measure",
        store=True,
    )
    is_less_than_minimum_quantity = fields.Boolean(
        compute="_compute_is_less_than_minimum_quantity",
        store=True,
    )

    @api.depends('product_variant_ids', 'product_variant_ids.qty_minimum')
    def _compute_qty_minimum(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.qty_minimum = template.product_variant_ids.qty_minimum
        for template in (self - unique_variants):
            template.qty_minimum = 0.0

    def _set_qty_minimum(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.qty_minimum = template.qty_minimum

    @api.depends("qty_available", "qty_minimum")
    def _compute_is_less_than_minimum_quantity(self):
        for rec in self:
            if rec.qty_available < rec.qty_minimum:
                rec.is_less_than_minimum_quantity = True
            else:
                rec.is_less_than_minimum_quantity = False
