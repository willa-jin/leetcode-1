# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):   ## D C
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        return self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):   ## recursively
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """ 
        # edge
        if not root:
            return True
        # process
        
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            else:
                return dfs(left.left, right.right) and (left.right, right.left)
        
        #recursion
        return dfs(root.left, root.right)
        
        
      # stack
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            elif left.val == right.val:
                stack.insert(0, (left.left, right.right))
                stack.insert(0, (left.right, right.left))
         return True
