class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最大化每对中的较小值之和，那么肯定是每对中两个数字大小越接近越好，
        因为如果差距过大，而我们只取较小的数字，那么大数字就浪费掉了。
        只需要给数组排个序，然后按顺序的每两个就是一对，
        我们取出每对中的第一个数即为较小值累加起来即可
        
        """
        n_s = sorted(nums)
        n = len(nums)
        
        result = 0
        i = 0
        while i < n:
			result += nums[i]
			i += 2
			
		return result
          
        
    
