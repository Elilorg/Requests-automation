import requests
import threading
import queue
from Packagename.controls import Bot
import logging 
from Packagename.externals_functions import sleep_random


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Add the handler to the logger

# Set propagate to False for all the handlers of the root logger








error_logger = logging.getLogger("errors")
error_handler = logging.FileHandler("./logs/Errors/errors.log")
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.DEBUG)

q = queue.Queue()


def launch() : 

    bot = Bot(headless=False, _name=q.get())
    bot.demarrer()

for i in range(7) : 
    q.put(f"BOT {i}")
    threading.Thread(target=launch).start()
    sleep_random(1, 2)