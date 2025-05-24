# bot.py
from binance.client import Client
from binance.enums import *
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logger.info("Bot initialized on Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            side_enum = SIDE_BUY if side == 'BUY' else SIDE_SELL

            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=str(price),
                    timeInForce=TIME_IN_FORCE_GTC
                )
            elif order_type == 'STOP_LIMIT':
                if stop_price is None or price is None:
                    logger.error("Stop price and limit price must be provided for STOP_LIMIT order")
                    return None
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_STOP_LOSS_LIMIT,
                    quantity=quantity,
                    price=str(price),
                    stopPrice=str(stop_price),
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                logger.error(f"Unsupported order type: {order_type}")
                return None

            logger.info(f"Order placed: {order}")
            return order

        except Exception as e:
            logger.error(f"Error placing order: {e}")
            return None
