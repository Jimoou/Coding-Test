import sys


def check(here):
    for i in range(here):
        if col[here] == col[i]: return False
        if abs(col[here] - col[i]) == here - i: return False
    return True


def solve(here):
    if here == N: return 1
    ret = 0
    for i in range(N):
        col[here] = i
        if check(here):
            ret += solve(here + 1)
        col[here] = -1
    return ret


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    col = [-1]*N
    print(solve(0))