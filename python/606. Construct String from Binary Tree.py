class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
		# recursively 
		
		if not t:  # 退出条件
			return ''
			
		s = str(t.val)
		left = self.tree2str(t.left)
		right = self.tree2str(t.right)
		
		if not t.left and not t.right: # both left and right are null, leaf
			return s
		if not t.right: # right is null --> '()' can be ignore
			return s + '(' + left + ')'
		
		return s + '(' + left + ')' +  '(' + right + ')'
		
        
