import sys


def PrimeNums(n):
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

    prime_Nums = PrimeNums(N)

    end = 0
    curSum = 0
    count = 0

    for start in range(len(prime_Nums)):
        while curSum < N and end < len(prime_Nums):
            curSum += prime_Nums[end]
            end += 1

        if curSum == N:
            count += 1

        curSum -= prime_Nums[start]

    print(count)