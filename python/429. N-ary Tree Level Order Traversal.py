"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        
        level order traversal similar like # 102
        """
		answer = []
		
		if not root:
			return answer
			
		level = [root]
		
		while level:
			answer.append([node.val for node in level])
			tmp = []
			for node in level:
				tmp.extend(node.children)
			level = [leaf for leaf in tmp if leaf]
		
		return answer
			
		
