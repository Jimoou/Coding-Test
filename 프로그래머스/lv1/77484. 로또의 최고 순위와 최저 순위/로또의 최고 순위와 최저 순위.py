def solution(lottos, win_nums):
    answer = []
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    answer.append(7-count-lottos.count(0) if 0 in lottos or count != 0 else 6)
    answer.append(6 if count == 0 else 7-count)
    return answer