import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cnt = 0
    if N % 5 == 0:
        print(N // 5)
    else:
        while N > 0:
            N -= 3
            cnt += 1
            if N % 5 == 0:
                cnt += N // 5
                print(cnt)
                break
            elif N == 1 or N == 2:
                print(-1)
                break
            elif N == 0:
                print(cnt)
                break
