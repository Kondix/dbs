import random
import math
from point import point

class pool:
    gather = []
    def __init__(self, objcnt):
        for i in range (1, objcnt):
            self.gather.append(point())
    def getgather(self):
        return self.gather
