import sys

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    end = 0
    sum = 0
    length = sys.maxsize

    for start in range(N):
        while sum < S and end < N:
            sum += A[end]
            end += 1
        if sum >= S:
            if length > end-start:
                length = end-start
        sum -= A[start]

    print(length if length != sys.maxsize else 0)
