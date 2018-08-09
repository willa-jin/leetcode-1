# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # https://leetcode.com/articles/intersection-two-linked-lists/
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # two points
        # the idea is if you switch head, the possible difference between length would be countered. 
        # On the second traversal, they either hit or miss. 
        
        #A:      a1 → a2               | a1 → a2
        #       ↘             ↗           ↘
        #         c1 → c2 → c3 |             c1 
        #       ↗             ↘             ↗  
        #B:   b1 → b2 → b3             | b1 → b2 → b3

        if not headA or not headB:
            return None
        a, b = headA, headB
        ans = None
        while a or b:
            if not a:
                a = headB
            if not b:
                b = headA
            if a == b and not ans:
                ans = a
            a, b = a.next, b.next
        return ans
