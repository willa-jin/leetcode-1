class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
		
		n = bin(N)[2:]
		
		index = [i for i, num in enumerate(n) if num == '1']
		
		distance = 0
		
		if len(index) == 1:
			return distance
			
		for i in range(len(index) - 1):
			distance = max(distance, index[i + 1] - index[i])
			
		return distance
