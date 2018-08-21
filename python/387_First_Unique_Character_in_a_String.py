class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hash_map = {}
        
        for index, l in enumerate(s):
            if l in hash_map.keys():
                hash_map[l].append(index)
            else:
                hash_map[l] = [index]
                
        once = [value[0] for key, value in hash_map.items() if len(value) == 1]
        
        if len(once) == 0:
            return -1
        
        return min(once)
          
      
    
