# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "SLUTION :: Custom addons",
    "summary": "Custom addons for only slution project",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "author": "Ecosoft Co., Ltd",
    "license": "AGPL-3",
    "website": "https://ecosoft.co.th",
    "depends": [
        "hr",
        "purchase",
        "sale_stock",
        "account_operating_unit",
        "account_check_deposit",
        "l10n_th_amount_to_text",
        "partner_fax",
        "report_context",
    ],
    "data": [
        "account_invoice_form/data/paper_format.xml",
        "account_invoice_form/data/report_data.xml",
        "account_invoice_form/report/account_invoice_form.xml",
        "account_invoice_form/report/report_invoice.xml",
        "hr_salesperson/report/sale_report_views.xml",
        "hr_salesperson/report/account_invoice_report_views.xml",
        "hr_salesperson/views/sale_views.xml",
        "hr_salesperson/views/res_partner_views.xml",
        "hr_salesperson/views/account_move_views.xml",
        "hr_salesperson/views/account_payment_views.xml",
        "sale_ext/views/sale_views.xml",
        "purchase_ext/views/purchase_views.xml",
        "billing_report/data/paper_format.xml",
        "billing_report/data/report_data.xml",
        "billing_report/security/ir.model.access.csv",
        "billing_report/security/billing_report_security.xml",
        "billing_report/report/slu_billing_report.xml",
        "billing_report/wizards/billing_report_wizard.xml",
        "billing_report/views/account_move_views.xml",
        "billing_report/views/account_payment_views.xml",
        "account_check_deposit_ext/views/account_payment_views.xml",
        "account_check_deposit_ext/views/account_move_views.xml",
        "account_check_deposit_ext/views/account_deposit_views.xml",
        "account_ext/views/account_move_views.xml",
        "stock_ext/views/stock_quant_views.xml",
        "stock_ext/views/product_views.xml",
        "sale_form/data/paperformat_data.xml",
        "sale_form/data/report_data.xml",
        "sale_form/report/quotation_form.xml",
        "purchase_form/data/paperformat_data.xml",
        "purchase_form/data/report_data.xml",
        "purchase_form/report/purchase_form.xml",
        "base_ext/views/res_company_views.xml",
    ],
    "installable": True,
}
