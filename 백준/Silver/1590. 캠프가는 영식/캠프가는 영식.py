import sys

if __name__ == '__main__':
    N, T = map(int, sys.stdin.readline().split())

    # S = 버스의 시작시간
    # I = 간격
    # C = 대수

    temp = []
    for _ in range(N):
        S, I, C = map(int, sys.stdin.readline().split())
        timeTable = [S + I * i for i in range(C)]
        if timeTable[-1] < T:
            continue
        start = 0
        end = C - 1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            if timeTable[mid] >= T:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        temp.append(timeTable[result] - T)
    print(min(temp) if temp else - 1)