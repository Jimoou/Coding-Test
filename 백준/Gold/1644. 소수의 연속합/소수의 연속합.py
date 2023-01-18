import sys


def primeNums(n):
    A = [True for i in range(n + 1)]
    B = []
    for i in range(2, int(n ** 0.5) + 1):
        if A[i]:
            j = 2
            while i * j <= N:
                A[i * j] = False
                j += 1
    for k in range(2, n + 1):
        if A[k]:
            B.append(k)
    return B


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    prime_nums = primeNums(N)

    end = 0
    primeSum = 0
    cnt = 0

    for start in range(len(prime_nums)):
        while primeSum < N and end < len(prime_nums):
            primeSum += prime_nums[end]
            end += 1

        if primeSum == N:
            cnt += 1

        primeSum -= prime_nums[start]

    print(cnt)
