# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype
        ## use two pointers fast and slow. fast two space
        
        fast = slow = head
        
        while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
              
        return slow
        
