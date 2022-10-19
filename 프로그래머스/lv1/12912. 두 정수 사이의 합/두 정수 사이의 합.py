def solution(a, b):
    if a > b:
        return sum(range (b, a+1))
    elif a < b:
        return sum(range (a, b+1))
    elif a == b:
        return a