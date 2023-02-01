def solution(sides):
    sides.sort(reverse=True)
    if sides[1] + sides[2] <= sides[0]:
        return 2
    else:
        return 1