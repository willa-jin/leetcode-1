class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
		# 海伦公式
		
		def area(p1, p2, p3):
			(x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
			s = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 -y2))
			return s
			
		return max(area(a, b, c) for a, b, c in  itertools.combinations(points, 3))
