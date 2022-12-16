import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    minSum = sys.maxsize

    liquid1 = 0
    liquid2 = 0
    liquid3 = 0

    A.sort()

    for start in range(N - 2):
        mid = start + 1
        end = N - 1

        while mid < end:
            curSum = A[start] + A[mid] + A[end]
            if abs(curSum) < minSum:
                minSum = abs(curSum)
                liquid1 = A[start]
                liquid2 = A[mid]
                liquid3 = A[end]

            if curSum > 0:
                end -= 1
            else:
                mid += 1

    print(liquid1, liquid2, liquid3)
