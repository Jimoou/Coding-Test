if __name__ == '__main__':
    N, M = map(int, input().split())

    chessBoard = []
    for _ in range(N):
        chessBoard.append(input())

    result = 8*8
    for n in range(N - 7):
        for m in range(M - 7):
            BW, WB = 0, 0
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0 and chessBoard[n+i][m+j] != 'W':
                        BW += 1
                    elif (i + j) % 2 == 1 and chessBoard[n+i][m+j] != 'B':
                        BW += 1
                    WB = 64 - BW
            result = min(result,BW)
            result = min(result,WB)

    print(result)