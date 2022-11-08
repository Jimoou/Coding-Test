if __name__ == '__main__':
    N, M = map(int, input().split())
    rectangular = []
    square_Size = []
    for _ in range(N):
        rectangular.append(input())
    for x in range(N):
        for y in range(M):
            vertex = rectangular[x][y]
            for length in range(max(M, N)):
                if x + length < N and y + length < M:
                    if vertex == rectangular[x][y + length] and vertex == rectangular[x + length][y] and vertex == rectangular[x + length][y + length]:
                        square_Size.append((length + 1) ** 2)
    print(max(square_Size))