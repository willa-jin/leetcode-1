class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
		Note:
       1 <= k <= n <= 30,000.
        Elements of the given array will be in the range [-10,000, 10,000].
        sliding window
		to determine the sum of elements from the index i+1 to the index i+k+1, 
		all we need to do is to subtract the element nums[i]from x and to add the element nums[i+k+1]to x.
        """
		answer = -10000 * len(nums)
		total = 0
		
		for i in range(len(nums)):
			total += nums[i]
			if i >= k:
				total -= nums[i - k]
			if i >= k -1:
				answer = max(answer, total / k)
		
		return answer
			
