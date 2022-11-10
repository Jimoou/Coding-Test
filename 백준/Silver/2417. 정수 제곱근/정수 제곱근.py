import math


def binary_search(n):
    left, right = 0, n - 1

    while left <= right:
        middle = (left + right) // 2

        if middle**2 < n:
            left = middle + 1
        else:
            right = middle - 1

    return left

if __name__ == "__main__":
    N = int(input())

    print(binary_search(N))