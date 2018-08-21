class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        return [[A[x][y] for x in range(0,len(A))] for y in range(0,len(A[0]))]
        """
		
		# list comprehension
		
		m = len(A)
		n = len(A[0])
		
		result = []
		
		for j in range(0, n):
			tmp = []
			for i in range(0, m):
				tmp.append(A[i][j])
			result.append(tmp)
		
		return result
