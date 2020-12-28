# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:57:43 2020

@author: Christian
"""

import numpy as np

from utils import distancePoints, cross2DPoints

def jarvis_march(S):
    if len(S) < 1:
        return []
    pointOnHull = min(S)
    i = 0
    P = [None] * len(S)
    endPoint = None
    while True:
        P[i] = pointOnHull
        endPoint = S[0]
        for j in range(len(S)):
            crossVal = cross2DPoints(P[i], endPoint, S[j])
            if endPoint == pointOnHull or crossVal < 0: # Counter clock wise
                endPoint = S[j]
            elif crossVal == 0 and distancePoints(P[i], endPoint) < distancePoints(P[i], S[j]):
                endPoint = S[j]
        i = i + 1
        pointOnHull = endPoint
        if endPoint == P[0]:
            break
    return P[0:i]

if __name__ == "__main__":
    points = [[0, 0], [1, 1], [2, 0], [0.5, 0.5]]
    #points = [[0, 0], [1, 0], [0, 1], [1, 1]]
    print(jarvis_march(points))

