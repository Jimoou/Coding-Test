import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))



    A.sort()
    count = 0
    for i in range(N):
        tmp = A[:i] + A[i + 1:]
        start = 0
        end = len(tmp) - 1
        while start < end:
            sum = tmp[start] + tmp[end]
            if sum == A[i]:
                count += 1
                break
            if sum > A[i]:
                end -= 1
            else:
                start += 1
    print(count)