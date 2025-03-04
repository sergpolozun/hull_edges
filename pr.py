points = [
    tuple(map(int, point.split(',')))
    for point in input(
        "Введите координаты точек через пробел "
        "(например: 36,70 41,32 91,33 41,2 22,91 81,10 78,67 17,17 "
        "9,38 32,7 19,46 64,20 51,5 36,68 7,97 39,59 97,8 26,8 96,99 74,71): "
    ).split()
]


def sign(p1, p2, p3):
    sign = (p2[1]-p1[1])*p3[0]+(p1[0]-p2[0])*p3[1]-(p1[0]*p2[1]-p1[1]*p2[0])
    return sign


def result1(p1, p2, points):
    first_sign = None
    for p in points:
        if p == p1 or p == p2:
            continue
        s = sign(p1, p2, p)
        if s != 0:
            if first_sign is None:
                first_sign = s > 0
            elif (s > 0) != first_sign:
                return False
    return True


def result2(points):
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if result1(points[i], points[j], points):
                edges.append((points[i], points[j]))
    return edges


hull = result2(points)
print("Рёбра выпуклой оболочки:")
for edge in hull:
    print(edge)
