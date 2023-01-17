import sys


def solve(mid):
    ret = 0
    for i in range(M):
        ret += (A[i] + mid - 1) // mid
    if ret <= N:
        return False
    else:
        return True


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    A = []
    for _ in range(M):
        A.append(int(sys.stdin.readline()))

    start = 1
    end = max(A)
    while start < end:
        mid = (start + end) // 2
        if solve(mid):
            start = mid + 1
        else:
            end = mid

    print(end)
