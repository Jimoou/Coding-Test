import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = N-1
    count = 0

    A.sort()
    while start < end:
        if A[start] + A[end] == M:
            count +=1

        if A[start] + A[end] > M:
            end -= 1
        else:
            start += 1
    print(count)
