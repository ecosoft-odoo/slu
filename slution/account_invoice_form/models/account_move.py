# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_datas(self):
        self.ensure_one()
        sale_orders = self.mapped("invoice_line_ids.sale_line_ids.order_id")
        stock_move_lines = sale_orders.mapped("picking_ids.move_lines.move_line_ids")
        deposit_product_id = self.env['ir.config_parameter'].sudo().get_param('sale.default_deposit_product_id')

        datas = {
            "amount_subtotal": 0.00,
            "discount": 0.00,
            "deposit": 0.00,
            "amount_tax": self.amount_tax,
            "amount_total": self.amount_total,
        }
        # get invoice lines
        invoice_lines = []
        for line in self.invoice_line_ids:
            if line.product_id.id == int(deposit_product_id):
                datas["deposit"] += line.price_subtotal
            else:
                invoice_line = line._prepare_invoice_lines()
                lots = stock_move_lines.filtered(
                    lambda l: l.state == "done" and l.lot_id and l.product_id == line.product_id
                ).mapped("lot_id")
                if lots:
                    invoice_line["lots"] = [lot.name for lot in lots]
                invoice_lines.append(invoice_line)
                datas["amount_subtotal"] += invoice_line['price_subtotal']
        datas["invoice_lines"] = invoice_lines

        if datas["deposit"]:
            datas["amount_after_deposit"] = self.amount_untaxed
            discount = self.amount_untaxed - datas['deposit'] - datas['amount_subtotal']
            if discount:
                datas["discount"] = discount
                datas["amount_after_discount"] = datas["amount_subtotal"] + discount
        else:
            discount = self.amount_untaxed - datas["amount_subtotal"]
            if discount:
                datas["discount"] = discount
                datas["amount_after_discount"] = self.amount_untaxed
        return datas


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def _prepare_invoice_lines(self):
        return {
            "description": self.name,
            "quantity": self.quantity,
            "product_uom": self.product_uom_id.name,
            "price_unit": self.price_unit,
            "price_subtotal": self.quantity * self.price_unit,
            "lots": [],
        }
