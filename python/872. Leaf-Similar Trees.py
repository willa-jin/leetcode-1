# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def FindLeaf(tree):
			if not tree.left and not tree.right:
				return [tree.val]
				
			if not tree.left:
				return FindLeaf(tree.right)
				
			if not tree.right:
				return FindLeaf(tree.left)
				
			return FindLeaf(tree.left) + FindLead(tree.right)
		
		return FindLeaf(root1) == FindLeaf(root2)
          
