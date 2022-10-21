def solution(n, m):
    a = max (n, m)
    b = min (n, m)
    while b != 0:
        r = a % b
        a = b
        b = r
    return [a, n*m // a]
