# Junnan Shimizu
# CS337 - Project 6
# 4/3/22

import time


class SolutionTwoBWT:
    def __init__(self):
        self.flag = [False, False]

    def lock(self, thread_id):
        self.flag[thread_id] = True
        if thread_id == 1:
            while self.flag[0]:
                continue
        else:
            time.sleep(0.0001)
            while self.flag[1]:
                continue

    def unlock(self, thread_id):
        self.flag[thread_id] = False

