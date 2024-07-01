from threading import Thread
import time


def numbers():
    for i in range(1,11):
        print(i)
        time.sleep(1)


literals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def literal():
    for i in literals:
        print(i)
        time.sleep(1)


t1 = Thread(target=numbers)
t2 = Thread(target=literal)
t1.start()
t2.start()
t1.join()
t2.join()
