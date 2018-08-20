class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = (A + ' ' + B).split(' ')
        res = [[x, c.count(x)] for x in set(c)]
        
        return [r[0] for r in res if r[1] == 1]
 
 
 ## use collections.Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = collections.Counter((A + ' ' + B).split(' '))
        
        return [w for w in c if c[w] == 1]
 
