pg_user="odoo"
prod_db="SLUTION_TEST"
psql="psql -U $pg_user -d $prod_db"

# Sales
$psql -c "delete from sale_order_line";
$psql -c "delete from sale_order";

# Purchase
$psql -c "delete from purchase_order_line"
$psql -c "delete from purchase_order"

# Stock
$psql -c "delete from stock_move_line"
$psql -c "delete from stock_move"
$psql -c "delete from stock_picking"
$psql -c "delete from stock_inventory"
$psql -c "delete from stock_scrap"
$psql -c "delete from stock_quant"
$psql -c "delete from stock_valuation_layer"
$psql -c "delete from stock_production_lot"

# Accounting
$psql -c "delete from account_partial_reconcile";
$psql -c "delete from account_move_line"
$psql -c "delete from account_move"
$psql -c "delete from account_payment"
$psql -c "delete from account_check_deposit"
$psql -c "delete from tax_adjustments_wizard";

# Miscellaneous
$psql -c "delete from mail_mail";
$psql -c "delete from mail_message";
