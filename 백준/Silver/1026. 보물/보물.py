import sys

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort(reverse=True)
    B.sort()
    print(sum([x*y for x,y in zip(A,B)]))