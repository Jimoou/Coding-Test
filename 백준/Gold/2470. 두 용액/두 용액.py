n = int(input())
liquid = list(map(int, input().split(' ')))
liquid.sort()

left = 0
right = n - 1

min_Value = abs(liquid[left] + liquid[right])
result = [liquid[left], liquid[right]]

while left < right:
    left_val = liquid[left]
    right_val = liquid[right]

    mixed_Liquid = left_val + right_val

    if abs(mixed_Liquid) < min_Value:
        min_Value = abs(mixed_Liquid)
        result = [left_val, right_val]
        if min_Value == 0:
            break
            
    if mixed_Liquid < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])