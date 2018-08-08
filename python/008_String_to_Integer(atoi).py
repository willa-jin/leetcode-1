class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        try:
            s = str.lstrip()
            i = 0
            result = ''
            while i < length(s):
                if s[i] in '+-' and result == '': # the sign is only valid at the first position
                    result = s[i]
                    i += 1
				if 0 <= s[i] <= 9:
					result += s[i]
					i += 1
				else:
					break
			r = int(result)
			if r  < -2 ** 31:
				r = -2 ** 31
			elif r > 2 ** 31 -1:
				r = 2 ** 31 -1
			return r
		except:
			return 0
               



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.myAtoi("+-2")
