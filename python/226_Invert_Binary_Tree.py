# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # recursively
    #     if root is None:
    #         return None
    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root
    
    
    def invertTree(self, root):
        # iteratively
        
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            node = stack.pop() # BFS
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        
        return root
        
