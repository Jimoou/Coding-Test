import sys
from itertools import combinations

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().split())

    A = list(map(int, sys.stdin.readline().split()))

    A.sort()

    cnt = 0
    for i in range(1, N+1):
        arrSum = 0
        for j in combinations(A, i):
            if sum(j) == S:
                arrSum += 1
        cnt += arrSum
    print(cnt)
