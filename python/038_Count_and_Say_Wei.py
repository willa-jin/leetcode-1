class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # using itertools.groupby
        # s = '111221'
        # for digit, group in itertools.groupby(s):
        #      print(digit, list(group))
        # 1 ['1', '1', '1']
        # 2 ['2', '2']
        # 1 ['1']
        
        s = '1'
        
        for _ in range(n - 1):
            temp = []
            for digit, group in itertools.groupby(s):
                temp.extend(str(len(list(group))) + digit)
            s = ''.join(temp)
		return s
