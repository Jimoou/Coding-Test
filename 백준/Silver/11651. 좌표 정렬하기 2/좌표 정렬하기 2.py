import sys

if __name__ == "__main__":
    N = int(input())
    coord_list = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coord_list.append((x, y))
    coord_list.sort(key=lambda x : (x[1],x[0]))
    for coord in coord_list:
        print(coord[0], coord[1])