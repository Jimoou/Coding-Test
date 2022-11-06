def solution(dwarf_Heights, a, b):
    sum = 0
    for i in range(len(dwarf_Heights)):
        if i == a or i == b:
            continue
        else:
           sum += dwarf_Heights[i]
    return sum
if __name__ == '__main__':
    dwarf_Heights = []
    for i in range(0, 9):
        dwarf_Heights.append(int(input()))
    for a in range(len(dwarf_Heights)):
        for b in range(a+1,len(dwarf_Heights)):
            if solution(dwarf_Heights, a, b) == 100:
                n1 = a
                n2 = b
    dwarf_Heights.remove(dwarf_Heights[n2])
    dwarf_Heights.remove(dwarf_Heights[n1])
    dwarf_Heights.sort()
    for heights in dwarf_Heights:
        print(heights)