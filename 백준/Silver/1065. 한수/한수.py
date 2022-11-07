if __name__ == '__main__':
    N = int(input())
    count = 0
    if N < 100:
        count = N
    else:
        count = 99
        for num in range(100,N+1):
            N_Nums = list(str(num))
            if int(N_Nums[0]) - int(N_Nums[1]) == int(N_Nums[1]) - int(N_Nums[2]):
                count += 1
    print(count)