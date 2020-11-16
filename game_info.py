from multiprocessing import Process
import time
import requests
import math

import urllib3
urllib3.disable_warnings()

url = 'https://127.0.0.1:2999/liveclientdata/gamestats'

current_time = 0

def start_polling(q):

    while True:
        time.sleep(1)
        try:
            reply = requests.get(url, verify=False).json()
            game_time = math.floor(reply['gameTime'])
            print(game_time)
        except requests.ConnectionError:
            q.put(0)
            print('No connection')


if __name__ == '__main__':
    p = Process(target=start_polling)
    p.start()
    p.join()