# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def get_words(self):
        word_dict = {
            "header": {
                "company_name": {
                    "en": "C. SAHAMONGKOL ENGINEERING LTD., PART.",
                    "th": "ห้างหุ้นส่วนจำกัด ช. สหมงคล เอ็นจิเนียริ่ง "
                          "(สำนักงานใหญ่)",
                },
                "company_address": {
                    "en": "76/92-93 RATCHDAPISEK RD., BANGKOK-YAI, BANGKOK "
                          "10600 THAILAND",
                    "th": "76/92-93 ถ.รัชดาภิเษก แขวงวัดท่าพระ เขตบางกอกใหญ่ "
                          "กรุงเทพฯ 10600",
                },
                "company_phone": {
                    "en": "TEL: +662-457-0066 (AUTO 4579424-25)",
                    "th": "โทรศัพท์: 02-457-0066 (AUTO 4579424-25)",
                },
                "company_fax": {
                    "en": "FAX: +662-457-9428",
                    "th": "แฟกซ์: 02-457-9428",
                },
                "company_email": {
                    "en": "EMAIL: csm@csm.co.th",
                    "th": "อีเมล์: csm@csm.co.th",
                },
                "company_website": {
                    "en": "WEBSITE: http://www.csmmarine.com",
                    "th": "เว็บไซต์: http://www.csmmarine.com",
                },
                "company_tax_id": {
                    "en": "TAX-ID: 010 353 400 7815",
                    "th": "หมายเลขประจำตัวผู้เสียภาษี: 010 353 400 7815",
                },
                "title": {
                    "en": "PURCHASE ORDER",
                    "th": "ใบสั่งซื้อ",
                },
                "name": {
                    "en": "Name:",
                    "th": "ชื่อ:",
                },
                "company": {
                    "en": "Company:",
                    "th": "บริษัท:",
                },
                "tax_id": {
                    "en": "Tax-ID:",
                    "th": "หมายเลขประจำตัวผู้เสียภาษี:",
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
                "po_no": {
                    "en": "PO No.:",
                    "th": "เลขที่สั่งซื้อ:",
                },
                "payment_term": {
                    "en": "Payment Term:",
                    "th": "เงื่อนไขชำระเงิน:",
                },
                "ship_via": {
                    "en": "Ship Via:",
                    "th": "วิธีจัดส่ง:",
                },
                "shipping_date": {
                    "en": "Shipping Date:",
                    "th": "วันกำหนดส่ง:",
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
                "remark": {
                    "en": "Remark:",
                    "th": "หมายเหตุ:",
                },
                "subtotal": {
                    "en": "Subtotal",
                    "th": "รวมเป็นเงิน",
                },
                "discount": {
                    "en": "Discount",
                    "th": "ส่วนลด",
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
                "requested_by": {
                    "en": "Requested by",
                    "th": "ผู้ขอซื้อ",
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
