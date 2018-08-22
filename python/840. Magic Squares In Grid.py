class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        #思路：从1到9取值，那么最中间的数必是5，只要从1，1到n-1,n-1遍历，如果满足值为5就进行判断
        """
		m,n = len(grid), len(grid[0])
		result = 0
		
		def isMagic(i, j):
			for x, y in [(-1, -1), (-1, 0) , (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
				if grid[i+x][j+y] > 9 or grid[i+x][j+y] < 1:
					return False
			return grid[i-1][j-1] + grid[i+1][j+1] == grid[i+1][j-1] + grid[i-1][j+1] == grid[i][j+1] +grid[i][j-1] == grid[i+1][j] + grid[i-1][j]
			
		for i in range(1, m-1):
			for j in range(1, n-1):
				if grid[i, j] == 5 and isMagic(i, j):
					result += 1
					
		return result
		
