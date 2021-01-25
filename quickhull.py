import numpy as np

def quickhull(points):
    if(len(points) < 2):
        return points
    
    min = points[0]
    max = points[0]

    for pt in points:
        if(pt[0] < min[0] or (pt[0] == min[0] and pt[1] < min[1])):
            min = pt
        if(pt[0] > max[0] or (pt[0] == max[0] and pt[1] > max[1])):
            max = pt

    if(min[0] == max[0]):
        return [min, max]

    global middle
    middle = [(min[0] + max[0]) / 2, (min[1] + max[1]) / 2]
    
    pointsAbove = []
    pointsBelow = []

    for pt in points:
        if(pt == min or pt == max):
            continue
        if(aboveLine(pt, min, max)):
            pointsAbove.append(pt)
        else:
            pointsBelow.append(pt)

    result = [min] + subsetQuickhull(pointsAbove, min, max) + [max] + subsetQuickhull(pointsBelow, min, max)
    
    result.sort(key=angle)

    return result

    #start = 0
    #for i in range(len(result)):
        #if((points[0] == result[0]) and (points[1] == result[1])):
            #start = i

    #output = []

    #for i in range(start, len(result)):
    #    output.append(result[i])
    
    #for i in range(start):
    #    output.append(result[i])


def angle(point):
    dx = point[0] - middle[0]
    dy = point[1] - middle[1]
    return np.arctan2(dy, dx)

def aboveLine(point, lineLeft, lineRight):
    if(lineLeft[0] > lineRight[0]):
        temp = lineRight
        lineRight = lineLeft
        lineLeft = temp
    ptDX = point[0] - lineLeft[0]
    ptDY = point[1] - lineLeft[1]
    lineDX = lineRight[0] - lineLeft[0]
    lineDY = lineRight[1] - lineLeft[1]
    if(lineDX == 0):
        if(ptDX < 0):
            return True
        else:
            return False
    if(ptDX == 0):
        if(ptDY > 0):
            return True
        else:
            return False
    if(ptDY > (lineDY / lineDX) * ptDX):
        return True
    return False

def squaredDistanceToLine(point, lineLeft, lineRight):
    lineDX = lineRight[0] - lineLeft[0]
    lineDY = lineRight[1] - lineLeft[1]

    if(lineDX == 0):
        return square(lineLeft[0] - point[0])
    if(lineDY == 0):
        return square(lineLeft[1] - point[1])
            
    lineSlope = lineDY / lineDX

    b = lineLeft[1] - lineLeft[0] * lineSlope

    perpendicularSlope = -1 / lineSlope

    pointB = point[1] - point[0] * perpendicularSlope

    #Now we have to solve for x: perpendicularSlope * x + pointB = lineSlope * x + b
    # perpSlope * x - lineSlope * x = b - pointB
    # (perpSlope - lineSlope) * x = b - pointB
    # x = (b - pointB) / (perpSlope - lineSlope)
    xOnLine = (b - pointB) / (perpendicularSlope - lineSlope)
    yOnLine = lineSlope * xOnLine + b

    return (square(point[0] - xOnLine) + square(point[1] - yOnLine))

def square(num):
    return num * num

def subsetQuickhull(points, linePointA, linePointB):
    if(len(points) < 2):
        return points
    
    furthestPoint = points[0]
    bestSqDist = squaredDistanceToLine(furthestPoint, linePointA, linePointB)
    
    for pt in points:
        sqDist = squaredDistanceToLine(pt, linePointA, linePointB)
        if(sqDist > bestSqDist):
            furthestPoint = pt
            bestSqDist = sqDist

    triangleCenterX = (furthestPoint[0] + linePointA[0] + linePointB[0]) / 3
    triangleCenterY = (furthestPoint[1] + linePointA[1] + linePointB[1]) / 3
    triCenter = [triangleCenterX, triangleCenterY]

    #Maybe the left point needs to come first for this to work...
    outsideA = not aboveLine(triCenter, linePointA, furthestPoint)
    outsideB = not aboveLine(triCenter, furthestPoint, linePointB)

    pointsA = []
    pointsB = []
    for pt in points:
        if(pt[0] == furthestPoint[0] and pt[1] == furthestPoint[1]):
            continue
        if(aboveLine(pt, linePointA, furthestPoint) == outsideA):
            pointsA.append(pt)
        elif(aboveLine(pt, furthestPoint, linePointB) == outsideB):
            pointsB.append(pt)

    return subsetQuickhull(pointsA, linePointA, furthestPoint) + [furthestPoint] + subsetQuickhull(pointsB, furthestPoint, linePointB)

    
import testing
if __name__ == "__main__":
    testinput2 = [[0.8, 0.4], [0.8, 0.6], [0.9, 0.8], [0.5, 0.7]]
    testing.checkAlgorithm(testinput2, quickhull)