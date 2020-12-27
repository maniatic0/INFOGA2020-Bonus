# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:32:33 2020

@author: Minmin and Christian
"""
import numpy as np

def is_right_turn(p0, p1, p2):
    e0 = [p1[0] - p0[0], p1[1] - p0[1]]
    e1 = [p2[0] - p1[0], p2[1] - p1[1]]
    return np.cross(e0, e1) < 0

def is_left_turn(p0, p1, p2):
    e0 = [p1[0] - p0[0], p1[1] - p0[1]]
    e1 = [p2[0] - p1[0], p2[1] - p1[1]]
    return np.cross(e0, e1) > 0

def generateUniformPoints(N):
    points = [None] * N
    for i in range(N):
        points[i] = list(np.random.rand(1, 2)[0])
    return points