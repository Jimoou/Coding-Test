import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 < N:
            start = mid + 1
        else:
            end = mid - 1
    print(start)
