import random
import math
import unittest
from point import point
from pool import pool
from dbscan import *

class stub_point:
    def __init__(self,ix , iy):	
        self.x = ix;
        self.y = iy; 

class TestDBScan(unittest.TestCase):
    test_gather = []

    def test_countRadiusInt(self):
        self.assertEqual(countRadius(stub_point(0, 0), stub_point(7, 0)), 7)

    def test_regionQuery(self):
        self.test_gather.append(stub_point(1,1))
        self.test_gather.append(stub_point(0,0))
        self.assertEqual(regionQuery(stub_point(0,0), 2, self.test_gather), self.test_gather)

    def test_regionQuery_2(self):
        self.assertEqual(regionQuery(stub_point(3,3), 1, self.test_gather), [])


