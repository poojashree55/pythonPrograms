def checkStraightLine(coordinates):
    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    print('x0, y0',x0, y0)
    print('x1, y1',x1, y1)

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
            return False

    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))
