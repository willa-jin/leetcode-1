''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        result = ''
        
        base = ord('A')  # change to 'a' is using lower case
        
        while n:
            n, r = divmod(n - 1, base)
            result += chr(base + r)
            
        return result[::-1]
