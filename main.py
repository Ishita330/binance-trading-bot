# main.py
from config import API_KEY, API_SECRET, SYMBOL
from bot import BasicBot

def get_user_input():
    while True:
        order_type = input("Enter order type (MARKET/LIMIT/STOP_LIMIT): ").strip().upper()
        if order_type not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
            print("Invalid order type. Please enter MARKET, LIMIT or STOP_LIMIT.")
            continue

        side = input("Enter side (BUY/SELL): ").strip().upper()
        if side not in ['BUY', 'SELL']:
            print("Invalid side. Please enter BUY or SELL.")
            continue

        try:
            quantity = float(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        price = None
        stop_price = None

        if order_type == 'LIMIT':
            try:
                price = float(input("Enter limit price: "))
                if price <= 0:
                    print("Price must be a positive number.")
                    continue
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue

        if order_type == 'STOP_LIMIT':
            try:
                stop_price = float(input("Enter stop price: "))
                if stop_price <= 0:
                    print("Stop price must be a positive number.")
                    continue
                price = float(input("Enter limit price: "))
                if price <= 0:
                    print("Limit price must be a positive number.")
                    continue
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue

        return order_type, side, quantity, price, stop_price

if __name__ == '__main__':
    bot = BasicBot(API_KEY, API_SECRET)
    order_type, side, quantity, price, stop_price = get_user_input()
    order = bot.place_order(SYMBOL, side, order_type, quantity, price, stop_price)

    if order:
        print("✅ Order placed successfully!")
        print(order)
    else:
        print("❌ Failed to place order. Check logs.")
