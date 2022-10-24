def solution(sizes):
    length, height = 0, 0
    for i in range(len(sizes)):
        length = max(length, max(sizes[i]))
        height = max(height, min(sizes[i]))
    return length*height