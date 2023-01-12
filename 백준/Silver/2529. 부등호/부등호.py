import sys
from itertools import permutations

N = int(input())
A = list(map(str, sys.stdin.readline().split()))
Nums = [x for x in range(10)]
answerList = []
for num in permutations(Nums, N + 1):
    for i in range(len(num) - 1):
        check = False
        if A[i] == '>':
            if num[i] > num[i + 1]:
                check = True
        else:
            if num[i] < num[i + 1]:
                check = True
        if check == False:
            break
    if check == True:
        answerList.append(num)

print(''.join(str(n) for n in (max(answerList))))
print(''.join(str(n) for n in (min(answerList))))
