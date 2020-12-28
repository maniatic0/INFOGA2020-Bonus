import math
import random

import numpy as np

def generateUniformPoints(N):
    points = [None] * N
    for i in range(N):
        points[i] = list(np.random.rand(1, 2)[0])
    return points

UniformDistribution = ("Uniform Distribution", generateUniformPoints)

def generateBoxPoints(N):
    points = [None] * N
    for i in range(N-4):
        points[i] = list(np.random.rand(1, 2)[0])
    points[N-4] = [-1, -1]
    points[N-3] = [-1,  1]
    points[N-2] = [ 1, -1]
    points[N-1] = [ 1,  1]
    random.shuffle(points)
    return points

BoxDistribution = ("Box Distribution", generateBoxPoints)

def generateLineDistributionOrdered(N):
    points = [None] * N
    for i in range(N-1):
        points[i] = [i, i]
    points[N-1] = [N-1, 0]
    return points

LineOrderedDistribution = ("Line Ordered Distribution", generateLineDistributionOrdered)

def generateLineDistributionInverted(N):
    points = generateLineDistributionOrdered(N)
    points.reverse()
    return points

LineInvertedDistribution = ("Line Inverted Distribution", generateLineDistributionInverted)

def generateLineDistributionShuffled(N):
    points = generateLineDistributionOrdered(N)
    random.shuffle(points)
    return points

LineShuffledDistribution = ("Line Shuffled Distribution", generateLineDistributionShuffled)

def generateLog2Distribution(N):
    points = [None] * N
    for i in range(N-1):
        points[i] = [i+1, math.log2(i+1)]
    points[N-1] = [N, 0]
    return points

Log2Distribution = ("Log2 Distribution", generateLog2Distribution)

def generateSquaredDistribution(N):
    points = [None] * N
    for i in range(N-1):
        points[i] = [i, i * i]
    points[N-1] = [N-1, 0]
    return points

SquaredDistribution = ("Squared Distribution", generateSquaredDistribution)