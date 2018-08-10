class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https: // en.wikipedia.org / wiki / Digital_root
        if num < 10:
            return num
        return num - ((num - 1) / 9) * 9
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num >= 10:
            num = sum(int(n) for n in str(num))
            
        return num
    
