from itertools import permutations

N = int(input())
arr = [x for x in range(1,N+1)]
for num in permutations(arr, N):
    print(*num)