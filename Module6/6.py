import time
from threading import Thread
from datetime import datetime

t1 = datetime.now()
def get_thread(number):
    time.sleep(1)
    print(number, end='')

for i in range(1, 6):
    get_thread(i)
t2 = datetime.now()
print(f'\n{(t2-t1).total_seconds()}')

t3 = datetime.now()
threads = [Thread(target=get_thread, args=(i,)) for i in range(1, 6)]

for t in threads:
    t.start()
for t in threads:
    t.join()
t4 = datetime.now()
print(f'\n{(t4-t3).total_seconds()}')