# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:57:43 2020

@author: DEITY
"""

import numpy as np
from utils import is_left_turn

def graham_scan(points):
    
    def half_hull(points):
        half_hull = []
        for p in points:
            while len(half_hull) > 1 and not is_left_turn(half_hull[-2], half_hull[-1], p):
                half_hull.pop()
            half_hull.append(p)
        return half_hull
    
    sorted_points = sorted(points)
    upper_hull = half_hull(sorted_points)
    lower_hull = half_hull(reversed(sorted_points))
    return upper_hull[:-1] + lower_hull[:-1]

if __name__ == "__main__":
    points = [[0, 0], [1, 1], [2, 0]]
    print(graham_scan(points))
