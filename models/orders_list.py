from models.order import Order

order1 = Order("Sam", "06/07/2022", 5)
order2 = Order("Jacob", "27/06/2022", 10)
order3 = Order("Jim", "01/01/2021", 1)
order4 = Order("Jimmy", "01/01/2021", 2)

order_list = [order1, order2, order3, order4]

# def find_biggest_order():
#     biggest_order = Order(None, None, 0)
#     for order in order_list:
#         if order.quantity > biggest_order.quantity:
#             biggest_order = order
#     return biggest_order

# def find_smallest_order():    
#     smallest_order = None
#     for order in order_list:
#         if order.quantity < smallest_order:
#             smallest_order = order
#     return smallest_order







