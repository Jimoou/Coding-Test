import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline()))

    start = 0
    end = 1
    gap = sys.maxsize

    A.sort()
    while start < N and end < N:
        curGap = abs(A[start] - A[end])
        if gap > curGap >= M:
            gap = curGap

        if curGap < M:
            end += 1
            continue
        start += 1
    print(gap)