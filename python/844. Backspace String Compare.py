class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        
        using stack
        """
		def process(s):
			stack = []
			for _ in s:
				if _ != '#':
					stack.append(_)
				else:
					if stack:
						stack.pop()
			return stack
		
		return process(S) == process(T)
