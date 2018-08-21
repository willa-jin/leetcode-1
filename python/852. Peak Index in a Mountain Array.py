class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        n = len(A)
        
        i = 0
        
        while i < n:
			if A[i] < A[i + 1]:
				i += 1
			else:
				return i 
        
