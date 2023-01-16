import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))

        B.sort()

        cnt = 0
        for a in A:
            L = 0
            R = M - 1
            result = -1
            while L <= R:
                mid = (L + R) // 2
                if B[mid] < a:
                    result = mid
                    L = mid + 1
                else:
                    R = mid - 1
            cnt += result + 1
        print(cnt)
