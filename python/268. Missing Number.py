class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        total = (0 + n) *(n + 1) / 2
        
        return int(total - sum(nums))
        
        
