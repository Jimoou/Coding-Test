def solution(dots):
    diagnol = []
    for i in range(len(dots)-1):
        for j in range(i+1,len(dots)):
            value = (dots[i][1]-dots[j][1]) /(dots[i][0]-dots[j][0])
            if value in diagnol:
                return 1
            else:
                diagnol.append(value)
    return 0