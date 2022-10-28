def solution(nums):
    if len(nums)//2 <= int(len(set(nums))):
        return len(nums)//2
    elif len(nums)//2 >= int(len(set(nums))):
        return int(len(set(nums)))
    else:
        return 1