from utils import naming


def format_orders(orders, user_lang):
    formatted_orders = []
    for order in orders:
        courier_name = order['Courier'] if order['Courier'] else "No one took this order"
        order_text = (
            f"{naming.order_id[user_lang]}: {order['id']}\n"
            f"{naming.order_status[user_lang]}: {order['Status']}\n"
            f"{naming.courier[user_lang]}: {courier_name}\n"
            f"{naming.client[user_lang]}: {order['Customer']}\n"
            f"{naming.quantity[user_lang]}: {order['Quantity']}\n"
            f"{naming.price[user_lang]}: {order['Price']}\n"
            "--------------------------"
        )
        formatted_orders.append(order_text)
    
    return formatted_orders
