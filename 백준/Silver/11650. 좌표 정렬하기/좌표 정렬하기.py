if __name__ == '__main__':
    N = int(input())
    coordinates = []
    for _ in range (N):
        x, y = map(int, input().split())
        coordinates.append((x, y))
    coordinates.sort()
    for loc in coordinates:
        print(loc[0],loc[1])