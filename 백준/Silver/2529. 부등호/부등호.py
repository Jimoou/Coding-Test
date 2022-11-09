import sys
from itertools import permutations

K = int(input())
inequalities = list(map(str, sys.stdin.readline().split()))
integerList = [x for x in range(10)]
answerList = []
for num in permutations(integerList, K + 1):
    for x in range(len(num)-1):
        check = False
        if inequalities[x] == '>':
            if num[x] > num[x+1]:
                check = True
        else:
            if num[x] < num[x+1]:
                check = True
        if check == False:
            break
    if check == True:
        answerList.append(num)

print(''.join(str(n) for n in (max(answerList))))
print(''.join(str(n) for n in (min(answerList))))
