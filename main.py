import random
import math
import unittest
from point import point
from pool import pool
from dbscan import *
from test import *
            

m_pool = pool(100)
m_gather = m_pool.getgather()
print('Init DONE')
DBSCAN(10, 5, m_gather)
print('Function DONE')

for b in m_clusters:
    print("NEW CLUSTER---------------------")
    print(len(b))
    for a in b:
        print(a.x, " ", a.y, " ", a.r)
print("NOISE---------------------")
for b in m_clusters:
    for a in b:
        if a.is_noise:
            print(a.x, " ", a.y, " ", a.r)

print("\n\n**********TEST************")
suite = unittest.TestLoader().loadTestsFromTestCase(TestDBScan)
unittest.TextTestRunner(verbosity=2).run(suite)

