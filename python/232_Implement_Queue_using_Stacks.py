# class Queue(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack1 = []
#         self.stack2 = []
#
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         while len(self.stack1) > 0:
#             curr = self.stack1.pop()
#             self.stack2.append(curr)
#         self.stack1.append(x)
#         while len(self.stack2) > 0:
#             curr = self.stack2.pop()
#             self.stack1.append(curr)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.stack1.pop()
#
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.stack1[-1]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stack1) == 0



class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.temp_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.main_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        
        while self.main_stack:
            self.temp_stack.append(self.main_stack.pop())
        ret = self.temp_stack.pop()
        
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
        
        return ret


    def peek(self):
        """
        :rtype: int
        """
        while self.main_stack:
            self.temp_stack.append(self.main_stack.pop())
        ret = self.temp_stack[-1]
        
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
            
        return ret

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.main_stack) == 0
