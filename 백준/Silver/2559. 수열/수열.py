import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    temps = list(map(int, sys.stdin.readline().split()))

    end = 0
    interval_sum = 0
    max_sum = sum(temps[:K])

    for start in range(N):
        while end < start+K and start + K <= N:
            interval_sum += temps[end]
            end += 1
        if interval_sum > max_sum:
            max_sum = interval_sum
        if start + K >= N:
            break
        interval_sum -= temps[start]

    print(max_sum)