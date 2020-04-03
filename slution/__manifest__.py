# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "SLUTION :: Custom addon",
    "summary": "Custom addon for only slution project",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "author": "Ecosoft Co., Ltd",
    "license": "AGPL-3",
    "website": "https://ecosoft.co.th",
    "depends": ["hr", "sale", "account"],
    "data": [
        "report/sale_report_views.xml",
        "report/account_invoice_report_views.xml",
        "views/sale_views.xml",
        "views/res_partner_views.xml",
        "views/account_move_views.xml"],
    "installable": True,
}
