import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int,sys.stdin.readline().split()))
    pSum = [0 for i in range(N+1)]
    for i in range(1, N + 1):
        pSum[i] = pSum[i - 1] + A[i-1]

    for i in range(M):
        B, C = map(int, sys.stdin.readline().split())
        print(pSum[C] - pSum[B - 1])
