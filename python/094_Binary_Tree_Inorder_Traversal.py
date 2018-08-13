# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     # recursively
    #     res = []
    #     self.do_inorderTraversal(res, root)
    #     return res
    #
    # def do_inorderTraversal(self, res, curr):
    #     if curr is None:
    #         return
    #     if curr.left is not None:
    #         self.do_inorderTraversal(res, curr.left)
    #     res.append(curr.val)
    #     if curr.right is not None:
    #         self.do_inorderTraversal(res, curr.right)

    # def inorderTraversal(self, root):
    #     # iteratively, but break the tree
    #     res = []
    #     if root is None:
    #         return res
    #     queue = [root]
    #     while len(queue) > 0:
    #         curr = queue.pop(0)
    #         if curr.left is None and curr.right is None:
    #             res.append(curr.val)
    #         else:
    #             if curr.right is not None:
    #                 queue.insert(0, curr.right)
    #                 curr.right = None
    #             queue.insert(0, curr)
    #             if curr.left is not None:
    #                 queue.insert(0, curr.left)
    #                 curr.left = None
    #     return res
    # def inorderTraversal(self, root):
    #     res = []
    #     stack = []
    #     while root is not None:
    #         stack.append(root)
    #         root = root.left
    #         while root is None:
    #             if len(stack) == 0:
    #                 return res
    #             root = stack.pop()
    #             res.append(root.val)
    #             root = root.right
    #     return res
    
    
    # divide and conqure
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if not node:
            return 
        self.helper(node.left, result) #  when reach the left leaf, node is null, return, execute resutl.append(leaf.val)
        result.append(node.val)
        self.helper(node.right, result)
        
        
    #先把迭代到最左边的叶子节点，把所有途中的root放进stack，当左边走不通了，开始往res里面存数，并往右边走。
    
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        result, currNode, stack = [], root, []
        
        while stack or currNode:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
                
           currNode = stack.pop()
           result.append(currNode.val)
           currNode = currNode.right
        
        return result
                
           



