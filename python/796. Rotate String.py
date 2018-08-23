class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        All rotations of A are contained in A+A. 
        Thus, we can simply check whether B is a substring of A+A.
        """
        
        if len(A) != len(B):
			return False
			
		if B in A + A:
			return True
		else:
			return False
        
