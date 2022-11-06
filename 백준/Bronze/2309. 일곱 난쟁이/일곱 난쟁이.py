def solution(a, b):
    sum = 0
    for num in range(9):
        if num not in [a, b]:
           sum += dwarf_Heights[num]
    return sum
if __name__ == '__main__':
    dwarf_Heights = []
    for _ in range(9):
        dwarf_Heights.append(int(input()))
    dwarf_Heights.sort()
    
    n1,n2 = 0,0
    for a in range(9):
        for b in range(a+1,9):
            if solution(a, b) == 100:
                n1 = a
                n2 = b
                
    for heights in dwarf_Heights:
        if heights not in [dwarf_Heights[n1],dwarf_Heights[n2]]:
            print(heights)
