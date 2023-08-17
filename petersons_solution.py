# Junnan Shimizu
# CS337 - Project 6
# 4/3/22


import time


class PetersonSolution:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0

    def lock(self, thread_id):
        if thread_id == 0:
            self.flag[0] = True
            self.turn = 1
            while self.turn == 1 and self.flag[1]:
                continue
        else:
            self.flag[1] = True
            self.turn = 0
            time.sleep(0.000001)
            while self.turn == 0 and self.flag[0]:
                continue

    def unlock(self, thread_id):
        if thread_id == 0:
            self.flag[0] = False
        else:
            self.flag[1] = False



