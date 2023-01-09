import sys


def solution(i, j):
    sum = 0
    for k in range(9):
        if k not in [i,j]:
            sum += A[k]
    return sum


if __name__ == '__main__':
    A = []
    for _ in range(9):
        A.append(int(sys.stdin.readline()))
    A.sort()
    n1, n2 = 0, 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if solution(i, j) == 100:
                n1 = i
                n2 = j

    for i in range(len(A)):
        if i not in [n1, n2]:
            print(A[i])
