# Junnan Shimizu
# CS337 - Project 6
# 4/3/22

import threading
import time

from bakery_solution import BakerySolution
from solution_two import SolutionTwo

x = 0


def increment():
    global x
    x += 1


def thread1_task(lock, my_num):
    global turn

    for _ in range(3000):
        lock.lock(my_num)
        increment()
        lock.unlock(my_num)


def thread2_task(lock, my_num):
    global turn

    for _ in range(3000):
        lock.lock(my_num)
        increment()
        lock.unlock(my_num)


def thread3_task(lock, my_num):
    global turn

    for _ in range(3000):
        lock.lock(my_num)
        increment()
        lock.unlock(my_num)


def main_task():
    global x

    x = 0

    # create a lock
    lock = BakerySolution(3)

    t1 = threading.Thread(target=thread1_task, args=(lock, 0,))
    t2 = threading.Thread(target=thread2_task, args=(lock, 1,))
    t3 = threading.Thread(target=thread3_task, args=(lock, 2,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


for i in range(10):
    main_task()
    print("Iteration {0}: x = {1}".format(i, x))