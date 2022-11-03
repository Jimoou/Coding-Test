from itertools import islice


def solution(survey, choices):
    type_Board = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        type = list(survey[i])
        if choices[i] < 4:
            type_Board[type[0]] += abs(choices[i]-4)
        elif choices[i] > 4:
            type_Board[type[1]] += choices[i]%4
    result = ''
    for i in range(4):
        i = 0
        temp = dict(islice(type_Board.items(),i+2))
        result += max(temp,key=temp.get)
        for i in temp:
            del type_Board[i]



    return result