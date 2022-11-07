if __name__ == '__main__':
    A, B = input().split()
    count_List = []
    for i in range(len(B)-len(A)+1):
        count = 0
        for j in range(len(A)):
            if A[j] == B[i+j]:
                count += 1
        count_List.append(count)
    print(len(A) - max(count_List))