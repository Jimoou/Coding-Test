def solution(today, terms, privacies):
    answer = []
    di = {}
    for i in range(len(terms)):
        temp = terms[i].split()
        di[temp[0]] = int(temp[1])

    todayTotal = today.split(".")
    intToday = int(todayTotal[0]) * 12 * 28 + (int(todayTotal[1])-1) * 28 + int(todayTotal[2])

    for i in range(len(privacies)):
        temp = privacies[i].split()
        date = temp[0].split(".")
        year = int(date[0])
        month = int(date[1]) + di.get(temp[1])
        day = int(date[2])
        total = year * 12 * 28 + (month-1) * 28 + day
        if total <= intToday:
            answer.append(i + 1)
    return answer