import random
import math
from point import point
from pool import pool

m_clusters = []

def countRadius(p, a):
    return math.sqrt((a.x - p.x)*(a.x - p.x)+(a.y - p.y)*(a.y - p.y))

def regionQuery(a_point, eps, p_gather):
    ret_points = []
    for p in p_gather:
        if countRadius(p, a_point) < eps:
            ret_points.append(p)
            p.r = countRadius(p, a_point)
    return ret_points

def expandCluster(p, neighb_points, clusterCnt, eps, MinPts, p_gather):
    temp = []
    m_clusters.append(temp)
    m_clusters[clusterCnt].append(p)
    p.is_member = 1
    for pp in neighb_points:
        if pp.is_visited == 0:
            pp.is_visited = 1
            nn_points = regionQuery(pp, eps, p_gather)
            if len(nn_points) >= MinPts:
                neighb_points += nn_points
        if pp.is_member == 0:
            m_clusters[clusterCnt].append(pp)
            pp.is_member = 1
                

def DBSCAN(eps, MinPts, p_gather):
    clusterCnt = -1
    for p in p_gather:
        if p.is_visited != 0:
            continue
        p.is_visited = 1
        neighb_points = regionQuery(p, eps, p_gather)
        if len(neighb_points) < MinPts:
            p.is_noise = 1 
        else:
            clusterCnt += 1
            expandCluster(p, neighb_points, clusterCnt, eps, MinPts, p_gather)
