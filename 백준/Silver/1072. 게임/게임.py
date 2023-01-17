import sys

if __name__ == '__main__':
    X, Y = map(int, sys.stdin.readline().split())
    Z = int((Y * 100 / X))

    start = 0
    end = 1000000000

    if Z >= 99:
        print(-1)
    else:
        while start <= end:
            mid = (start + end) // 2
            if int(((Y + mid) * 100) / (X + mid)) <= Z:
                start = mid + 1
            else:
                end = mid -1
        print(start)
