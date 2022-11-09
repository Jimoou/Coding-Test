import sys
from itertools import permutations

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
sumList = []
for num in permutations(arr, N):
    sum = 0
    for x in range(N-1):
        sum += abs(num[x]-num[x+1])
    sumList.append(sum)
print(max(sumList))