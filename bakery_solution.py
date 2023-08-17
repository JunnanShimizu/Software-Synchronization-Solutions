# Junnan Shimizu
# CS337 - Project 6
# 4/3/22

import time


class BakerySolution:
    def __init__(self, thread_count):
        self.choosing = [False] * thread_count
        self.tickets = [0] * thread_count
        self.thread_count = thread_count

    def lock(self, thread_id):
        self.choosing[thread_id] = True
        self.tickets[thread_id] = max(self.tickets) + 1
        self.choosing[thread_id] = False
        for i in self.choosing:
            time.sleep(0.0001)
            while self.choosing[i]:
                continue
            while self.tickets[i] != 0 and (self.tickets[i] < self.tickets[thread_id] or self.tickets[i] == self.tickets[thread_id] and i < thread_id):
                continue

    def unlock(self, thread_id):
        self.tickets[thread_id] = 0
