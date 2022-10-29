def solution(answers):
    sooPoza1 = [1, 2, 3, 4, 5]
    sooPoza2 = [2,1,2,3,2,4,2,5]
    sooPoza3 = [3,3,1,1,2,2,4,4,5,5]
    d = {1:0, 2:0, 3:0}
    for i in range (len(answers)):
        if sooPoza1[i%5] == answers[i]:d[1] += 1
        if sooPoza2[i%8] == answers[i]:d[2] += 1
        if sooPoza3[i%10] == answers[i]:d[3] += 1

    grade =	[k for k,v in d.items() if max(d.values()) == v]

    return grade