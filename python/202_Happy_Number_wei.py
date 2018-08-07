class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # https://en.wikipedia.org/wiki/Happy_number
        #after each time, they check for both halt conditions: reaching 1, and repeating a number. 
        #Everything else is book-keeping (for example, the Python example precomputes the squares of all 10 digits).
        
        seen_number = set()
        while n > 1 and n not in seen_number:
            seen_number.add(n)
            temp = [int(m)*int(m) for m in list(str(n))]
            n = sum(temp)
            
        return n == 1 
        
        
       
    #seen_numbers = set()
     #   while n > 1 and n not in seen_numbers:
     #       seen_numbers.add(n)
     #       n = sum(map(lambda x: int(x) * int(x), list(str(n))))
     #   return n == 1
    
    
