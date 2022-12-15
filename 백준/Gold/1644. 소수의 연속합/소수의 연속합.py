import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = [True for i in range(N + 1)]
    primeNums = []
    for i in range(2, int(N ** 0.5) + 1):
        if A[i]:
            j = 2
            while i * j <= N:
                A[i*j] = False
                j += 1

    for num in range(2, N + 1):
        if A[num]:
            primeNums.append(num)

    end = 0
    sum = 0
    count = 0
    for start in range(len(primeNums)):
        while sum < N and end < len(primeNums):
            sum += primeNums[end]
            end += 1
        if sum == N:
            count += 1
        sum -= primeNums[start]

    print(count)
