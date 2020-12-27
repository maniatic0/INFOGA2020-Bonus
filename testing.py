
import time
import sys
import copy
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d


def checkAlgorithm(S, algorithm):
    """Checks that an algorithm correctly calculated the convex hull, as well how long did it take in nano seconds"""
    points = np.array(S)
    hull_res = ConvexHull(points)
    
    SCopy = copy.deepcopy(S)
    tic = time.perf_counter_ns()
    hull = algorithm(SCopy)
    toc = time.perf_counter_ns()

    real_hull_size = len(hull_res.vertices)
    if real_hull_size != len(hull):
        print(f"Different Hull Sizes {real_hull_size} != {len(hull)} (Scipy vs {algorithm.__name__})", file=sys.stderr)
        return (False, toc - tic)

    for i in range(real_hull_size):
        if list(hull_res.points[hull_res.vertices[i]]) == hull[0]:
            for j in range(len(hull)):
                P = list(hull_res.points[hull_res.vertices[(i + j) % real_hull_size]])
                if P != hull[j]:
                    print(f"Different Points {P} != {hull[j]} (Scipy vs {algorithm.__name__})", file=sys.stderr)
                    return (False, toc - tic)

    return (True, toc - tic)

def testTime(points, algorithms):
    results = [(False, -1)] * len(algorithms)
    for i, algorithm in enumerate(algorithms):
        results[i] = checkAlgorithm(points, algorithm)
    return results

def testSize(attempts, generator, size, algorithms):
    results = [0] * len(algorithms)
    for attempt in range(attempts):
        print(f"Generator '{generator.__name__}' Size: {size} Attempt: {attempt + 1}/{attempts}")
        points = generator(size)
        temp_res = testTime(points, algorithms)
        for i, (check, time) in enumerate(temp_res):
            results[i] = results[i] + time
            if not check:
                with open(f"{generator.__name__}_{size}_{attempt}_{algorithms[i].__name__}.txt", 'w') as f:
                    f.write(points)
                    f.close()

    for i in range(len(algorithms)):
        results[i] = results[i] / attempts
    return results

def testGenerator(attempts, generator, sizes, algorithms):
    results = {}

    for algorithm in algorithms:
        results[algorithm.__name__] = {}
    
    for size in sizes:
        temp_res = testSize(attempts, generator, size, algorithms)
        for i, time in enumerate(temp_res):
            results[algorithms[i].__name__][size] = time

    return results
