from flask import Blueprint, render_template
from .models import Products, Transactions
from .database import db_session

dash = Blueprint(
    'dashboard',
    __name__,
    url_prefix=''
)

TITLE = 'Happy Hour'

@dash.route('/welcome/dashboard')
def main():
    product = Products.query.all()
    rows = db_session.query(Products).count()
    return render_template('dashboard/dashboard.html', title=TITLE, products=product, row=rows)


@dash.route('/inventory')
def inventory():
    product = Products.query.all()
    return render_template('dashboard/inventory.html', title=TITLE, products=product)


@dash.route('/inventory/add-stock', methods=['GET'])
def new_stock():
    return "hello, world"


@dash.route('/report/generate/new')
def report():
    transactions = Transactions.query.all()
    return render_template('dashboard/report.html', title=TITLE, transactions=transactions)

@dash.route('/report/generate/download')
def generate_report():
    return 'hello world'


@dash.route('/update/settings')
def settings():
    return render_template('dashboard/settings.html', title=TITLE)


@dash.route('/market/sell')
def sell():
    return render_template('dashboard/sell.html', title=TITLE)


@dash.route('/warehouse/goods/list-all')
def checked_in():
    products = Products.query.all()
    return render_template('dashboard/item_warehouse.html', title=TITLE, product=products)