import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    indexA, indexB = 0, 0
    answer_list = []

    while indexA <= N and indexB <= M:
        if indexA == N and indexB == M:
            break
        if indexA == N:
            print(B[indexB])
            indexB += 1
        elif indexB == M:
            print(A[indexA])
            indexA += 1
        elif A[indexA] < B[indexB]:
            print(A[indexA])
            indexA += 1
        elif A[indexA] < B[indexB]:
            indexA += 1
        else:
            print(B[indexB])
            indexB += 1
