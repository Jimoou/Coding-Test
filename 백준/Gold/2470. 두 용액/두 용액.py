import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = N-1

    max_sum = sys.maxsize

    liquid1 = 0
    liquid2 = 0

    A.sort()

    while start < end:
        curSum = A[start] + A[end]
        if abs(curSum) < max_sum:
            max_sum = abs(curSum)
            liquid1 = A[start]
            liquid2 = A[end]

        if curSum > 0:
            end -= 1
        else:
            start += 1

    print(liquid1, liquid2)