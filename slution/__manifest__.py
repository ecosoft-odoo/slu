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
    "depends": ["hr", "purchase", "sale_stock"],
    "data": [
        "account_invoice_form/data/paper_format.xml",
        "account_invoice_form/data/report_data.xml",
        "account_invoice_form/report/account_invoice_form.xml",
        "hr_salesperson/report/sale_report_views.xml",
        "hr_salesperson/report/account_invoice_report_views.xml",
        "hr_salesperson/views/sale_views.xml",
        "hr_salesperson/views/res_partner_views.xml",
        "hr_salesperson/views/account_move_views.xml",
        "hr_salesperson/views/account_payment_views.xml",
        "purchase_ext/views/purchase_views.xml",
        "billing_report/data/paper_format.xml",
        "billing_report/data/report_data.xml",
        "billing_report/security/ir.model.access.csv",
        "billing_report/report/slu_billing_report.xml",
        "billing_report/wizards/billing_report_wizard.xml",
        "billing_report/views/account_move_views.xml",
        "billing_report/views/account_payment_views.xml"],
    "installable": True,
}
