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
            start = 0
            end = M-1
            result = -1
            while start <= end:
                mid = (start+end)//2

                if B[mid] < a:
                    result = mid
                    start = mid + 1
                else:
                    end = mid - 1
            cnt += result + 1
        print(cnt)