import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    pPix = [0 for i in range(M)]
    pSum = [0 for i in range(N+1)]

    pPix[0] = 1

    for i in range(1, N + 1):
        pSum[i] = pSum[i - 1] + A[i - 1]
        pPix[pSum[i] % M] += 1

    cnt = 0
    for i in pPix:
        cnt += i*(i-1)//2
    print(cnt)
