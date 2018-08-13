# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
     def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    # divide and conquer
        if not root:
            return []
        result = []
        self.helper(root,result)
        return result
    
    def helper(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.helper(node.left, result)
        self.helper(node.right, result)


    def preorderTraversal(self, root):
        # stack
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

