import bisect
import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    pSumA = []
    pSumB = []

    for i in range(N):
        s = A[i]
        pSumA.append(s)
        for j in range(i+1,N):
            s += A[j]
            pSumA.append(s)

    for i in range(M):
        s = B[i]
        pSumB.append(s)
        for j in range(i + 1, M):
            s += B[j]
            pSumB.append(s)

    pSumA.sort()
    pSumB.sort()
    result = 0
    for i in range(len(pSumA)):
        left = bisect.bisect_left(pSumB, T - pSumA[i])
        right = bisect.bisect_right(pSumB, T - pSumA[i])
        result += right - left
    print(result)



