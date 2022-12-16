import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = N-1

    minSum = sys.maxsize

    liquid1 = 0
    liquid2 = 0

    while start < end:
        curSum = A[start] + A[end]
        if abs(curSum) < minSum:
            minSum = abs(curSum)
            liquid1 = A[start]
            liquid2 = A[end]

        if curSum > 0:
            end -= 1
        else:
            start += 1
    print(liquid1, liquid2)