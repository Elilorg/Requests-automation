

from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from Packagename.controls import Bot
import time 
from Packagename.externals_functions import sleep_random
from multiprocessing import Process, cpu_count

import logging

valider_log_level = logging.DEBUG
app_log_level = logging.DEBUG

logging.basicConfig(level=logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.getLogger().handlers[0].propagate = False


error_logger = logging.getLogger("errors")
error_handler = logging.FileHandler("./logs/Errors/errors.log")
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.DEBUG)

def start_bot(i=0) : 
    bot=Bot(headless=True, _name=f"BOT {i}")
    bot.demarrer(limit=20)
    


num_cores = cpu_count() - 1  # Leave one core for other system processes


processes = []
for i in range(num_cores):
    sleep_random(1, 3)
    p = Process(target=start_bot, args=[i])
    processes.append(p)
    p.start()


print("CONTINUE")
time.sleep(30)


for i in processes : 
    i.join()
















