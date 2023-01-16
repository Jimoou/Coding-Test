import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    A.sort()

    sum = int(sys.maxsize)

    liquidA=0
    liquidB=0
    liquidC=0

    for start in range(N-2):
        end = N-1
        mid = start + 1
        while mid < end:
            curSum = A[start] + A[mid] + A[end]
            if abs(curSum) < sum:
                sum = abs(curSum)
                liquidA=A[start]
                liquidB=A[mid]
                liquidC=A[end]

            if curSum > 0:
                end -= 1
            elif curSum == 0:
                liquidA = A[start]
                liquidB = A[mid]
                liquidC = A[end]
                break
            else:
                mid += 1

    print(liquidA, liquidB, liquidC)