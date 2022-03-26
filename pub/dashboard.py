from flask import Blueprint, redirect, render_template, request, url_for
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
    status = {
        'delivered': 'Delivered',
        'return': 'Return',
        'inprogress': 'In Progress',
        'pending': 'Pending'
    }
    return render_template('dashboard/inventory.html', title=TITLE, products=product, status=status)


@dash.route('/inventory/add-stock', methods=['GET', 'POST'])
def new_stock():
    if request.method == 'POST':
        name = request.form.get('itm-name')
        stock = request.form.get('itm-qyt')
        price = request.form.get('itm-price')
        tax = request.form.get('itm-tax')
        status = request.form.get('status')

        new_product = Products(name=name, stock=stock, price=price, tax=tax, status=status)
        db_session.add(new_product)
        db_session.commit()
        return redirect(url_for('dashboard.inventory'))
    

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
    return render_template('dashboard/item_warehouse.html', title=TITLE, products=products)