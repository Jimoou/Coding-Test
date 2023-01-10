import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    max = sys.maxsize
    cnt = 0
    for i in range(max):
        if "666" in str(i):
            cnt += 1
            if cnt == N:
                print(i)
                break