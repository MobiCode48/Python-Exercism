def equilateral(sides: list) -> bool:
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False

    return sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides: list) -> bool:
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False

    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides: list) -> bool:
    return not equilateral(sides) and not isosceles(sides)
