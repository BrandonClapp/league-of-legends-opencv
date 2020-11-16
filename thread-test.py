import threading
import time

num = 1


def add():
    while True:
        global num
        num += 1
        time.sleep(0.1)
        print('thread', num)


t = threading.Thread(target=add)
t.start()
t.join

while True:
    time.sleep(0.1)
    print('main', num)

print(num)
