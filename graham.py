# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:57:43 2020

@author: DEITY
"""

import numpy as np

def graham_scan(points):
    def is_right_turn(p0, p1, p2):
        e0 = [p1[0] - p0[0], p1[1] - p0[1]]
        e1 = [p2[0] - p1[0], p2[1] - p1[1]]
        return np.cross(e0, e1) < 0
    
    def half_hull(points):
        half_hull = []
        for p in points:
            while len(half_hull) > 1 and not is_right_turn(half_hull[-2], half_hull[-1], p):
                half_hull.pop()
            half_hull.append(p)
        return half_hull
    
    sorted_points = sorted(points)
    upper_hull = half_hull(sorted_points)
    lower_hull = half_hull(reversed(sorted_points))
    return upper_hull[:-1] + lower_hull[:-1]

points = [[0, 0], [1, 1], [2, 0]]
print(graham_scan(points))