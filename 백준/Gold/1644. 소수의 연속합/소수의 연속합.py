import sys


def PrimeNums(n):
    root = int(n ** 0.5)
    if root % 2 == 0:
        root += 1
    sieve = [None] * (n // 2 + 2)
    ret = [2]
    for i in range(1, (root + 1) // 2):
        if not sieve[i]:
            ret.append(2 * i + 1)
            t = 2 * i + 1
            for j in range((t * t) // 2, n // 2 + 1, t):
                sieve[j] = True
    for i in range((root + 1) // 2, n // 2 + 1):
        if not sieve[i]:
            ret.append(2 * i + 1)
    if ret[-1] > n:
        ret.pop()
    return ret


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