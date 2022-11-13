import sys

if __name__ == '__main__':
    X, Y = map(int, sys.stdin.readline().split())
    Z = int((Y*100) / X)
    L = 0
    R = 1000000000
    mid = 0
    if Z >= 99:
        print(-1)
    else:
        while L <= R:
            mid = (L + R) // 2
            if int(((Y + mid) * 100) / (X + mid)) <= Z:
                L = mid + 1
            else:
                R = mid - 1
        print(L)
