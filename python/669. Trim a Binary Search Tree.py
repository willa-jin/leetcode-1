# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
		每一层的Condition有三种：
		root.val小于区间的lower bound L，则返回root.right subtree传上来的root，
		这里就变相的'删除'掉了当前root和所有root.left的node
		root.val大于区间的upper bound R，则返回root.left subtree传上来的root
		满足区间，则继续递归
		当递归走到叶子节点的时候，我们向上返回root，这里return root的定义是：
		返回给parent一个区间调整完以后的subtree
        """
		
		if not root:
			return root:
			
		if root.val < L :
			return self.trimBST(root.right, L, R)
		
		if root.val > R:
			return self.trimBST(root.left, L, R)
			
		root.left = self.trimBST(root.left, L, R)
		root.right = self.trimBST(root.right, L, R)
		
		return root
		
		
