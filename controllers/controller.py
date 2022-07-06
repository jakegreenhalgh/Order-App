from flask import render_template
from app import app
from models.orders_list import *

@app.route('/orders')
def index():
    return render_template('index.html', title="Order List", all_orders=order_list)

@app.route('/orders/<int:order_num>')
def order(order_num):
    order_to_display = order_list[order_num - 1] 
    return render_template('order.html', title=f"Order {order_num}", order=order_to_display)

# @app.route('/orders/biggest_order')
# def big_list():
#     return render_template('index.html', title="Biggest Order", all_orders=find_biggest_order())

# @app.route('/orders/smalllest_order')
# def big_list():
#     return render_template('index.html', title="Smallest Order", all_orders=find_smallest_order())