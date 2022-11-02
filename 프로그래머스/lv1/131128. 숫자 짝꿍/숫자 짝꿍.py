def solution(X, Y):
    combi = []
    for i in set(X)&set(Y):
         for j in range(min(X.count(i),Y.count(i))):
            combi.append(i)
    if not combi: return "-1"
    if max(combi) == "0" : return "0"
    return ''.join(sorted(combi,reverse=True))