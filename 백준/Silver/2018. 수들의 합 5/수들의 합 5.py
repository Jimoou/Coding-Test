import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    left = 1
    right = 1
    sum = 1
    answer = 0
    while left <= right:
        if sum == N:
            answer += 1
        if sum < N:
            right += 1
            sum += right
        elif sum >= N:
            sum -= left
            left += 1

    print(answer)