# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
class Solution(object):
    # def swapPairs(self, head):
    #     current = last = last2 = head
    #     while current is not None:
    #         nex = current.next
    #         if current == last.next:
    #             last.next = nex
    #             current.next = last
    #             if last == head:
    #                 head = current
    #             else:
    #                 last2.next = current
    #             last2 = last
    #             last = nex
    #         current = nex
    #     return head
    
    
    # To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, need to change three reference
	
	def swapPairs(self, head):
		dummyHead = ListNode(-1)
		dummyHead.next = head
		
		prev = dummyHead
		
		while prev.next and prev.next.next:
			a = prev.next
			b = prev.next.next
			prev.next, b.next, a.next  = b, a, b.next
			prev = a
		return dummyHead.next
	
	

        
