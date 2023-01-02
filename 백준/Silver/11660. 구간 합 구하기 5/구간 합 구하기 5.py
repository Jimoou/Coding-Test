import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    B = []
    for _ in range(N):
        A = list(map(int, sys.stdin.readline().split()))
        B.append(A)
    prefixSum = [[0 for j in range(N + 1)] for i in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefixSum[i][j] = prefixSum[i][j - 1] + prefixSum[i - 1][j] - prefixSum[i - 1][j - 1] + B[i - 1][j - 1]

    for i in range(M):
        x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
        print(prefixSum[x2][y2] - prefixSum[x1-1][y2] - prefixSum[x2][y1-1] + prefixSum[x1-1][y1-1])
