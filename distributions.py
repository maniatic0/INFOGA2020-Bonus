import math
import random

import numpy as np

def generateUniformDistribution(N):
    points = [None] * N
    for i in range(N):
        points[i] = list(np.random.rand(1, 2)[0])
    return points

UniformDistribution = ("Uniform Distribution", generateUniformDistribution)

def generateBoxDistribution(N):
    points = [None] * N
    for i in range(N-4):
        points[i] = list(np.random.rand(1, 2)[0])
    points[N-4] = [-1, -1]
    points[N-3] = [-1,  1]
    points[N-2] = [ 1, -1]
    points[N-1] = [ 1,  1]
    random.shuffle(points)
    return points

BoxDistribution = ("Box Distribution", generateBoxDistribution)

def generateNGonDistribution(N):
    points = [None] * N
    for i in range(N):
        angle = 2 * math.pi / N * i - math.pi / 2
        points[i] = [math.cos(angle), math.sin(angle)]
    return points

NGonDistribution = ("N Gon Distribution", generateNGonDistribution)

def generateRepeatedDistributionOrdered(N):
    points = [None] * N
    points[0] = [0, 0]
    points[1] = [0, 1]
    points[2] = [1, 0]
    for i in range(3, N):
        points[i] = [0, 0]
    return points

RepeatedOrderedDistribution = ("Repeated Ordered Distribution", generateRepeatedDistributionOrdered)

def generateRepeatedDistributionInverted(N):
    points = generateRepeatedDistributionOrdered(N)
    points.reverse()
    return points

RepeatedInvertedDistribution = ("Repeated Inverted Distribution", generateRepeatedDistributionInverted)

def generateRepeatedDistributionShuffled(N):
    points = generateRepeatedDistributionOrdered(N)
    random.shuffle(points)
    return points

RepeatedShuffledDistribution = ("Repeated Shuffled Distribution", generateRepeatedDistributionShuffled)

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

def generateLog2DistributionOrdered(N):
    points = [None] * N
    for i in range(N-1):
        points[i] = [i+1, math.log2(i+1)]
    points[N-1] = [N, 0]
    return points

Log2OrderedDistribution = ("Log2 Ordered Distribution", generateLog2DistributionOrdered)

def generateLog2DistributionInverted(N):
    points = generateLog2DistributionOrdered(N)
    points.reverse()
    return points

Log2InvertedDistribution = ("Log2 Inverted Distribution", generateLog2DistributionInverted)

def generateLog2DistributionShuffled(N):
    points = generateLog2DistributionOrdered(N)
    random.shuffle(points)
    return points

Log2ShuffledDistribution = ("Log2 Shuffled Distribution", generateLog2DistributionShuffled)

def generateSquaredDistributionOrdered(N):
    points = [None] * N
    for i in range(N-1):
        points[i] = [i, i * i]
    points[N-1] = [N-1, 0]
    return points

SquaredOrderedDistribution = ("Squared Ordered Distribution", generateSquaredDistributionOrdered)

def generateSquaredDistributionInverted(N):
    points = generateSquaredDistributionOrdered(N)
    points.reverse()
    return points

SquaredInvertedDistribution = ("Squared Inverted Distribution", generateSquaredDistributionInverted)

def generateSquaredDistributionShuffled(N):
    points = generateSquaredDistributionOrdered(N)
    random.shuffle(points)
    return points

SquaredShuffledDistribution = ("Squared Shuffled Distribution", generateSquaredDistributionShuffled)
