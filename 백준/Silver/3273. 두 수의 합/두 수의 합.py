import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    X = int(sys.stdin.readline())

    interval_sum = 0
    count = 0
    start = 0
    end = N - 1
    A.sort()
    while start < end:
        interval_sum = A[start] + A[end]
        if interval_sum == X:
            count += 1
        if interval_sum <= X:
            start += 1
        else:
            end -= 1

    print(count)
