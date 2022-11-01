def solution(board, moves):
    bucket = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop()
                        bucket.pop()
                        cnt += 2
                break
    return cnt