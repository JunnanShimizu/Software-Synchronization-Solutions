# Junnan Shimizu
# CS337 - Project 6
# 4/3/22

class SolutionOne:
    def __init__(self):
        self.turn = 1

    def lock(self, thread_id):
        while self.turn != thread_id:
            continue

    def unlock(self, thread_id):
        if thread_id == 1:
            self.turn = 2
        else:
            self.turn = 1
