import sys


def dfs(x):
    if len(S) == M:
        print(*S)
        return

    for i in range(x, N + 1):
        S.append(i)
        dfs(i)
        S.pop()


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    S = []
    dfs(1)
