class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        five, ten, twenty = [], [], []
        
        for b in bills:
			if b == 5:
				five.append(b)
			elif b == 10:
				if five:
					five.pop()
					ten.append(b)
				else:
					return False
			elif b == 20:
				if ten and five:
					ten.pop()
					five.pop()
					twenty.append(b)
				elif len(five) >= 3:
					five.pop()
					five.pop()
					five.pop()
				else:
					return False
		return True
            
