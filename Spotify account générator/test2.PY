import requests
import threading
import queue
import logging

logger = logging.getLogger("THELOGGER")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(threadName)s: %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


q = queue.Queue()

for i in open("proxys.txt").readlines() : 
    q.put(i)
    

valid_proxies = queue.Queue()
def check() : 

    global q
    while not q.empty() : 
        proxy = q.get().replace("\n", "")
        print(proxy)
        logger.debug(f"proxy tested : {proxy}")
        

        proxies = { 
                    "http"  : proxy, 
                    "https" : proxy, 
                    }
        
        try : 
            r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=3)
            if r.status_code == 200 : 
                q.put(proxy)
                print(r.json())
        except Exception as e : 
            print(e)
            logger.debug("Proxy failed")


threads = []


for _ in range(10) : 
    thread = threading.Thread(target=check)
    thread.start()
    threads.append(thread)

for i in threads : 
    i.join()

print(valid_proxies.queue)


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def target_function():
    logging.debug('Inside the target function.')

if __name__ == '__main__':
    thread = threading.Thread(target=target_function)
    thread.start()
    thread.join()






