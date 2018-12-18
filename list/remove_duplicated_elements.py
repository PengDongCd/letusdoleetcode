def remove_duplication(nums):
    l = len(nums)
    i = 0

    for j in range(0,l):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
    return i + 1