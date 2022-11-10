import sys

T = int(input())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())

    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    B.sort()

    count = 0
    for i in range(0,N):
        L = 0
        R = M-1
        result = -1
        while L <= R:
            mid = (L + R) // 2
            if B[mid] < A[i]:
                result = mid
                L = mid + 1
            else:
                R = mid - 1
        count += result + 1
    print(count)