class Solution(object):
    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     # O(n^2)
    #     ls = len(nums)
    #     pos = 0
    #     while pos < ls:
    #         if nums[pos] == 0:
    #             curr = pos + 1
    #             while curr < ls:
    #                 if nums[curr] != 0:
    #                     temp = nums[curr]
    #                     nums[curr] = nums[pos]
    #                     nums[pos] = temp
    #                     break
    #                 curr += 1
    #         pos += 1

    def moveZeroes(self, nums):
        # O(n)
        # left, right two pointers, right went through nums, if nums[right] != 0, move to the left, left = left + 1
        
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
           right += 1



