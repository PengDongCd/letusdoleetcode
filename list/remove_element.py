class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        index = 0
        for j in range(l):
            if nums[j] != val:
                nums[index] = nums[j]
                index += 1
        return index
