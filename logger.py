# logger.py
import logging

def setup_logger():
    logger = logging.getLogger('BinanceBot')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('logs/bot.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
