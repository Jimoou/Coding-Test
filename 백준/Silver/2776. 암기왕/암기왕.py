import sys


def binary_search(num):
    L = 0
    R = N - 1
    while L <= R:
        mid = (L + R) // 2
        if num == note_No1[mid]:
            return 1
        elif num < note_No1[mid]:
            R = mid - 1
        else:
            L = mid + 1
    return 0


if __name__ == '__main__':
    T = int(input())
    for test in range(T):
        N = int(input())
        note_No1 = list(map(int, sys.stdin.readline().split()))
        M = int(input())
        note_No2 = list(map(int, sys.stdin.readline().split()))

        note_No1.sort()

        for num in note_No2:
            print(binary_search(num))
