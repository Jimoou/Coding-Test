def solution(a, b, n):
    sum = 0
    while n >= a:
        c = n//a*b
        n = n%a
        n = n+c
        sum += c
    return sum