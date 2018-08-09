# class Solution(object):
#     def isValid(self, s):
        
#
class Solution:
        def isValid(self, s):
                stack = []
                dic = {']' :'[', '}':'{', ')':'('}
                
                for c in s:
                        if c in dic.values():
                                stack.append(c)
                        elif c in dic.keys():
                                if stack == [] or dic[c] != stack.pop():
                                        return False
                        else:
                                return False
                return stack == []



    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False



   
           

        
