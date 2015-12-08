import random
import math

class point:
    def __init__(self):
        self.x = round(random.random()*100,2)
        self.y = round(random.random()*100,2)
        self.r = 0
        self.is_member = 0
        self.is_noise = 0
        self.is_visited = 0
    def getpoint(self):
        return [self.x, self.y]
    def setpoint(xi, yi):
        self.x = xi
        self.y = yi
