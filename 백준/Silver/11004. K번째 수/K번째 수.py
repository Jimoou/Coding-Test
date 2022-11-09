import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()
    print(A[K-1])