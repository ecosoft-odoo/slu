# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_words(self):
        self.ensure_one()
        word_dict = {
            "header": {
                "company_name": {
                    "en": self.company_id.name.upper(),
                    "th": self.company_id.company_registry,
                },
                "company_address": {
                    "en": " ".join(filter(
                        lambda l: l, [
                            self.company_id.street,
                            self.company_id.street2,
                            self.company_id.city,
                            self.company_id.state_id.name,
                            self.company_id.zip,
                            self.company_id.country_id.name])).upper(),
                    "th": " ".join(filter(
                        lambda l: l, [
                            self.company_id.street_th,
                            self.company_id.street2_th,
                            self.company_id.city_th,
                            self.company_id.state_th,
                            self.company_id.zip_th,
                            self.company_id.country_th])),
                },
                "company_phone": {
                    "en": "TEL: %s" % (self.company_id.phone, ),
                    "th": "โทรศัพท์: %s" % (self.company_id.phone, ),
                },
                "company_fax": {
                    "en": "FAX: %s" % (self.company_id.partner_id.fax, ),
                    "th": "แฟกซ์: %s" % (self.company_id.partner_id.fax, ),
                },
                "company_email": {
                    "en": "EMAIL: %s" % (self.company_id.email, ),
                    "th": "อีเมล์: %s" % (self.company_id.email, ),
                },
                "company_website": {
                    "en": "WEBSITE: %s" % (self.company_id.website, ),
                    "th": "เว็บไซต์: %s" % (self.company_id.website, ),
                },
                "company_tax_id": {
                    "en": "TAX-ID: %s" % (self.company_id.vat, ),
                    "th": "หมายเลขประจำตัวผู้เสียภาษี: %s" % (
                        self.company_id.vat, ),
                },
                "title": {
                    "en": "QUOTATION",
                    "th": "ใบเสนอราคา",
                },
                "name": {
                    "en": "Name:",
                    "th": "ชื่อลูกค้า:",
                },
                "company": {
                    "en": "Company:",
                    "th": "บริษัท:",
                },
                "tax_id": {
                    "en": "Tax-ID:",
                    "th": "Tax-ID:",
                },
                "address": {
                    "en": "Address:",
                    "th": "ที่อยู่:",
                },
                "email": {
                    "en": "Email:",
                    "th": "อีเมล์:",
                },
                "phone": {
                    "en": "Tel:",
                    "th": "โทรศัพท์:",
                },
                "fax": {
                    "en": "Fax:",
                    "th": "แฟกซ์:",
                },
                "date": {
                    "en": "Date:",
                    "th": "วันที่:",
                },
                "quotation_no": {
                    "en": "Quotation No:",
                    "th": "เลขที่:",
                },
                "price_validity": {
                    "en": "Price Validity:",
                    "th": "กำหนดยืนราคา:",
                },
                "payment_term": {
                    "en": "Payment Term:",
                    "th": "เงื่อนไขชำระเงิน:",
                },
                "description": {
                    "en": "Thank you for your inquiry. We have the pleasure "
                          "in offering you as the following detail.",
                    "th": "บริษัทมีความยินดีเสนอราคาอุปกรณ์ประกอบสำหรับ"
                          "เครื่องมืออิเล็กทรอนิกส์ทางทะเล "
                          "ตามที่ท่านได้สอบถามมายังบริษัท ดังนี้",
                },
            },
            "article": {
                "number": {
                    "en": "No.",
                    "th": "เลขที่",
                },
                "description": {
                    "en": "Description",
                    "th": "รายละเอียดสินค้า",
                },
                "quantity": {
                    "en": "Quantity",
                    "th": "จำนวน",
                },
                "unit_price": {
                    "en": "Unit Price",
                    "th": "ราคาต่อหน่วย",
                },
                "amount": {
                    "en": "Amount",
                    "th": "จำนวนเงิน",
                },
                "term_and_condition": {
                    "en": "Term & Condition:",
                    "th": "เงื่อนไข:",
                },
                "subtotal": {
                    "en": "Subtotal",
                    "th": "รวมเป็นเงิน",
                },
                "discount": {
                    "en": "Discount",
                    "th": "หักส่วนลด",
                },
                "after_discount": {
                    "en": "After Discount",
                    "th": "จำนวนเงินหลังหักส่วนลด",
                },
                "vat": {
                    "en": "Vat",
                    "th": "จำนวนภาษีมูลค่าเพิ่ม",
                },
                "grand_total": {
                    "en": "Grand Total",
                    "th": "จำนวนเงินรวมทั้งสิ้น",
                },
            },
            "footer": {
                "order_by": {
                    "en": "Order by",
                    "th": "ผู้อนุมัติซื้อ",
                },
                "prepared_by": {
                    "en": "Prepared by",
                    "th": "ผู้จัดทำ",
                },
                "authorized_signature": {
                    "en": "Authorized Signature",
                    "th": "ผู้มีอำนาจอนุมัติ",
                },
                "date": {
                    "en": "Date",
                    "th": "วันที่",
                },
            },
        }
        return word_dict
