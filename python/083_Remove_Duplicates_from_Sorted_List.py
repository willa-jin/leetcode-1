# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def deleteDuplicates(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None:
    #         return None
    #     temp = ListNode(2147483647)
    #     temp.next = head
    #     pos = head
    #     head = temp
    #     last = head
    #     while pos is not None:
    #         if last.val == pos.val:
    #             last.next = pos.next
    #         else:
    #             last = pos
    #         pos = pos.next
    #     return head.next

    def deleteDuplicates(self, head):
        if not head:
            return None
        
        pos = head
        
        while pos and pos.next:
            if pos.val == pos.next.val:
                pos.next = pos.next.next # it is ok that pos.next.next == None
            else:
                pos = pos.next
        return head

